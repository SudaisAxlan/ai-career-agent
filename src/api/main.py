from fastapi import FastAPI
from sqlmodel import SQLModel

from src.api.db_connection import engine

from src.api.routes.user import user_router
from src.api.routes.resume import resume_router
from src.api.routes.job_response import job_response_router
from src.api.routes.job_search import job_router
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.auth import auth_router



app = FastAPI(
    title="AI Career Agent"
)


app = FastAPI(title="AI Career Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
SQLModel.metadata.create_all(engine)


app.include_router(user_router)
app.include_router(resume_router)
app.include_router(job_response_router)
app.include_router(job_router)
app.include_router(auth_router)



@app.get("/")
def home():
    return {
        "message": "AI Career Agent API is running agaon"
    }
