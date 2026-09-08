from typing import List, Optional
from pydantic import BaseModel


# Request schema
class JobSearchRequest(BaseModel):
    resume_id: int
    job_title: str


# Single job result
class JobSearchResult(BaseModel):
    rank: int
    job_title: str
    company: str
    location: Optional[str] = None
    job_type: Optional[str] = None
    posted_date: Optional[str] = None
    description: Optional[str] = None
    required_skills: Optional[str] = None
    experience: Optional[str] = None
    salary: Optional[str] = None
    deadline: Optional[str] = None
    match_score: Optional[float] = None
    why_match: Optional[str] = None
    apply_url: str
    source: Optional[str] = None


# Response schema
class JobSearchResponse(BaseModel):
    user_id: int
    resume_id: int
    job_title: str
    jobs: List[JobSearchResult]