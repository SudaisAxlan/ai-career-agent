from sqlmodel import Session

from src.api.db_connection import engine
from src.api.model.resume import Resume


def create_resume(

    user_id: int,

    file_url: str,

    extracted_text: str

) -> Resume:

    with Session(engine) as session:

        resume = Resume(

            user_id=user_id,

            file_url=file_url,

            extracted_text=extracted_text

        )

        session.add(resume)

        session.commit()

        session.refresh(resume)

        return resume