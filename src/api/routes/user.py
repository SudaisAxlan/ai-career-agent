from fastapi import APIRouter, HTTPException

from src.api.schemas.user import UserCreate
from src.api.services.user_service import create_user


user_router = APIRouter(

    prefix="/users",

    tags=["Users"]

)


@user_router.post("/")

def register_user(user: UserCreate):

    try:

        new_user = create_user(user)

        return {

            "message": "User created successfully",

            "user": new_user

        }

    except ValueError as e:

        raise HTTPException(

            status_code=400,

            detail=str(e)

        )