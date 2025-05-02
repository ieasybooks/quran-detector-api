from pydantic import BaseModel, Field
from typing import Optional

from app.v1.models.ayah_match import AyahMatch


class OperationsResponse(BaseModel):
    annotated_text: Optional[str] = Field(
        None, title="Annotated Text",
        description="Diacriticized text with references, if 'annotate' was requested."
    )
    matches: Optional[list[AyahMatch]] = Field(
        None, title="Detected Ayaht",
        description="List of ayah matches, if 'detect' was requested."
    )
