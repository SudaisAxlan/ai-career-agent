from fastapi import APIRouter, UploadFile, File, HTTPException

from src.api.services.cloudinary_service import upload_resume
from src.api.services.pdf_service import pdf_parser
from src.api.services.resume_service import create_resume


resume_router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)


@resume_router.post("/{user_id}")
async def upload_user_resume(
    user_id: int,
    file: UploadFile = File(...)
):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    pdf_bytes = await file.read()

    if not pdf_bytes:
        raise HTTPException(
            status_code=400,
            detail="PDF file is empty."
        )

    file_url = upload_resume(
        pdf_bytes=pdf_bytes,
        filename=file.filename
    )

    extracted_text = pdf_parser(pdf_bytes)

    resume = create_resume(
        user_id=user_id,
        file_url=file_url,
        extracted_text=extracted_text
    )

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume.id,
        "filename": file.filename,
        "file_url": resume.file_url,
        "text_extracted": bool(extracted_text)
    }