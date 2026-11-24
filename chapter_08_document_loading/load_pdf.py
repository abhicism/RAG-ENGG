
"""Extract and print text from the sample FastAPI PDF."""

from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    pdf_path = Path(__file__).resolve().parent / "documents" / "fastapi_tutorial.pdf"
    reader = PdfReader(pdf_path)
    page_text = [page.extract_text() or "" for page in reader.pages]
    full_text = "\n".join(text for text in page_text if text.strip())

    if not full_text:
        raise ValueError(f"No extractable text found in {pdf_path}")

    print(full_text)


if __name__ == "__main__":
    main()
