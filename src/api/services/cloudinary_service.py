import cloudinary.uploader


def upload_resume(pdf_bytes: bytes, filename: str):

    result = cloudinary.uploader.upload(
        pdf_bytes,
        resource_type="image",
        folder="ai-career-agent/resumes",
        public_id=filename.rsplit(".", 1)[0],
        format="pdf"
    )


    return result["secure_url"]