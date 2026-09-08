from typing import Optional

from sqlmodel import SQLModel, Field


class Resume(SQLModel, table=True):

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    user_id: int

    file_url: str

    extracted_text: str