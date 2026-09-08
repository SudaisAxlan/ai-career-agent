from sqlmodel import SQLModel,Field

class JobSearch(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)

    user_id: int

    job_title: str