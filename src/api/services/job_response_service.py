from sqlmodel import Session

from src.api.db_connection import engine
from src.api.model.job import JobResponse
from src.api.schemas.job import JobResponseCreate


def create_job_response(
    job_data: JobResponseCreate
) -> JobResponse:

    with Session(engine) as session:

        job = JobResponse(

            user_id=job_data.user_id,

            job_title=job_data.job_title,

            company=job_data.company,

            location=job_data.location,

            job_type=job_data.job_type,

            description=job_data.description,

            required_skills=job_data.required_skills,

            experience=job_data.experience,

            salary=job_data.salary,

            posted_date=job_data.posted_date,

            deadline=job_data.deadline,

            match_score=job_data.match_score,

            why_match=job_data.why_match,

            apply_url=job_data.apply_url,

            source=job_data.source

        )

        session.add(job)

        session.commit()

        session.refresh(job)

        return job