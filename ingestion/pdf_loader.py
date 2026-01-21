import fitz
import uuid
import re
from pathlib import Path
from typing import List

from .document import Document


def _clean_text(text: str) -> str:
    """
    Normalize PDF text:
    - remove excessive whitespace
    - fix hyphenated line breaks
    - normalize newlines
    """
    text = text.replace("-\n", "")  # fix word breaks
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def load_pdf(
    pdf_path: str,
    source_type: str = "paper"
) -> List[Document]:
    """
    Load a PDF and return one Document per page.
    """
    pdf_path = Path(pdf_path)
    assert pdf_path.exists(), f"File not found: {pdf_path}"

    documents: List[Document] = []
    pdf = fitz.open(pdf_path)

    for page_idx, page in enumerate(pdf):
        raw_text = page.get_text("text")
        if not raw_text or len(raw_text.strip()) < 100:
            continue

        clean_text = _clean_text(raw_text)

        doc = Document(
            doc_id=str(uuid.uuid4()),
            text=clean_text,
            metadata={
                "source_type": source_type,
                "file_name": pdf_path.name,
                "file_path": str(pdf_path),
                "page_number": page_idx + 1,
                "total_pages": pdf.page_count
            }
        )
        documents.append(doc)

    return documents
