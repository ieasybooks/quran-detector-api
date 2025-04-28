from pydantic import BaseModel, Field
from typing import Optional

from app.v1.models.verse_match import VerseMatch


class OperationsResponse(BaseModel):
    annotated_text: Optional[str] = Field(
        None, title="Annotated Text",
        description="Diacriticized text with references, if 'annotate' was requested."
    )
    matches: Optional[list[VerseMatch]] = Field(
        None, title="Detected Verses",
        description="List of verse matches, if 'detect' was requested."
    )