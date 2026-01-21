from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Document:
    """
    Atomic unit flowing through the RAG pipeline.
    """
    doc_id: str
    text: str
    metadata: Dict
    parent_doc_id: Optional[str] = None
