import pymupdf


def pdf_parser(pdf_bytes: bytes) -> str:

    pdf = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text