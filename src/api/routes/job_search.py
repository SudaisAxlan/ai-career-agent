from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from src.api.db_connection import engine
from src.api.model.resume import Resume
from src.api.schemas.job_search import (
    JobSearchRequest,
    JobSearchResult,
    JobSearchResponse
)

from src.api.schemas.job import JobResponseCreate
from src.api.services.job_response_service import create_job_response

from src.agents.graph import agent


job_router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@job_router.post(
    "/search/{user_id}",
    response_model=JobSearchResponse
)
def search_jobs(
    user_id: int,
    request: JobSearchRequest
):

    # --------------------------------
    # 1. Get user's resume
    # --------------------------------

    with Session(engine) as session:

        resume = session.exec(
            select(Resume)
            .where(Resume.id == request.resume_id)
            .where(Resume.user_id == user_id)
        ).first()

    if not resume:

        raise HTTPException(
            status_code=404,
            detail="Resume not found."
        )


    # --------------------------------
    # 2. Create LangGraph state
    # --------------------------------

    state = {
        "user_question": request.job_title,
        "user_profile": resume.extracted_text,
        "search_plan": "",
        "search_results": [],
        "matched_jobs": [],
        "response": ""
    }


    # --------------------------------
    # 3. Run LangGraph
    # --------------------------------

    result = agent.invoke(state)


    # --------------------------------
    # 4. Get matched jobs
    # --------------------------------

    matched_jobs = result.get(
        "matched_jobs",
        []
    )


    if not matched_jobs:

        raise HTTPException(
            status_code=404,
            detail="No matching jobs found."
        )


    # --------------------------------
    # 5. Save jobs to PostgreSQL
    # --------------------------------

    saved_jobs = []


    for job in matched_jobs:

        job_data = JobResponseCreate(

            user_id=user_id,

            job_title=job.get(
                "job_title",
                "Not available"
            ),

            company=job.get(
                "company",
                "Not available"
            ),

            location=job.get(
                "location"
            ),

            job_type=job.get(
                "job_type"
            ),

            description=job.get(
                "description"
            ),

            required_skills=job.get(
                "required_skills"
            ),

            experience=job.get(
                "experience"
            ),

            salary=job.get(
                "salary"
            ),

            posted_date=job.get(
                "posted_date"
            ),

            deadline=job.get(
                "deadline"
            ),

            match_score=job.get(
                "match_score"
            ),

            why_match=job.get(
                "why_match"
            ),

            apply_url=job.get(
                "apply_url",
                "Not available"
            ),

            source=job.get(
                "source"
            )
        )


        saved_job = create_job_response(
            job_data
        )


        saved_jobs.append(
            saved_job
        )


    # --------------------------------
    # 6. Return response
    # --------------------------------

    return JobSearchResponse(

        user_id=user_id,

        resume_id=request.resume_id,

        job_title=request.job_title,

        jobs=[
            JobSearchResult(
                rank=index + 1,
                job_title=job.job_title,
                company=job.company,
                location=job.location,
                job_type=job.job_type,
                posted_date=job.posted_date,
                description=job.description,
                required_skills=job.required_skills,
                experience=job.experience,
                salary=job.salary,
                deadline=job.deadline,
                match_score=job.match_score,
                why_match=job.why_match,
                apply_url=job.apply_url,
                source=job.source
            )

            for index, job in enumerate(saved_jobs)
        ]
    )


