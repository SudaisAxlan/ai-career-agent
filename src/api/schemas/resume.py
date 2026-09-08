from pydantic import BaseModel


class ResumeResponse(BaseModel):

    id: int

    user_id: int

    file_url: str

    extracted_text: str