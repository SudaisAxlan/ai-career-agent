from sqlmodel import Session

from src.api.db_connection import engine
from src.api.model.job import Job


def create_job(
    search_id: int,
    job_data: dict
) -> Job:

    with Session(engine) as session:

        job = Job(
            search_id=search_id,
            title=job_data.get("title", ""),
            company=job_data.get("company", ""),
            location=job_data.get("location", ""),
            job_type=job_data.get("job_type"),
            posted_date=job_data.get("posted_date"),
            description=job_data.get("description"),
            requirements=job_data.get("requirements"),
            experience_required=job_data.get(
                "experience_required"
            ),
            salary=job_data.get("salary"),
            deadline=job_data.get("deadline"),
            match_score=job_data.get("match_score"),
            match_reason=job_data.get("match_reason"),
            apply_url=job_data.get("apply_url", ""),
            source=job_data.get("source")
        )

        session.add(job)
        session.commit()
        session.refresh(job)

        return job


def create_jobs(
    search_id: int,
    jobs: list[dict]
) -> list[Job]:

    created_jobs = []

    with Session(engine) as session:

        for job_data in jobs:

            job = Job(
                search_id=search_id,
                title=job_data.get("title", ""),
                company=job_data.get("company", ""),
                location=job_data.get("location", ""),
                job_type=job_data.get("job_type"),
                posted_date=job_data.get("posted_date"),
                description=job_data.get("description"),
                requirements=job_data.get("requirements"),
                experience_required=job_data.get(
                    "experience_required"
                ),
                salary=job_data.get("salary"),
                deadline=job_data.get("deadline"),
                match_score=job_data.get("match_score"),
                match_reason=job_data.get("match_reason"),
                apply_url=job_data.get("apply_url", ""),
                source=job_data.get("source")
            )

            session.add(job)

            created_jobs.append(job)

        session.commit()

        for job in created_jobs:
            session.refresh(job)

        return created_jobs