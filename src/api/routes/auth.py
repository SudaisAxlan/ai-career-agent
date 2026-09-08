from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from src.api.db_connection import engine
from src.api.model.user import User
from src.api.schemas.auth import LoginRequest


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth_router.post("/login")
def login(data: LoginRequest):

    with Session(engine) as session:

        user = session.exec(
            select(User)
            .where(User.email == data.email)
        ).first()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        if user.password != data.password:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        return {
            "message": "Login successful",
            "user_id": user.id,
            "name": user.name,
            "email": user.email
        }