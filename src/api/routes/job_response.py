from fastapi import APIRouter

from src.api.schemas.job import JobResponseCreate
from src.api.services.job_response_service import create_job_response


job_response_router = APIRouter(

    prefix="/job-responses",

    tags=["Job Responses"]

)


@job_response_router.post("/")

def save_job_response(job_data: JobResponseCreate):
    new_job = create_job_response(job_data)
    return {

        "message": "Job response saved successfully",

        "job": new_job

    }