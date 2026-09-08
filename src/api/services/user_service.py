from sqlmodel import Session, select

from src.api.db_connection import engine
from src.api.model.user import User
from src.api.schemas.user import UserCreate


def create_user(user_data: UserCreate) -> User:

    with Session(engine) as session:

        existing_user = session.exec(
            select(User)
            .where(User.email == user_data.email)
        ).first()

        if existing_user:

            raise ValueError(
                "User with this email already exists."
            )

        user = User(

            name=user_data.name,

            email=user_data.email,

            password=user_data.password

        )

        session.add(user)

        session.commit()

        session.refresh(user)

        return user