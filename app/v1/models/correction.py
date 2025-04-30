from pydantic import BaseModel, Field


class Correction(BaseModel):
    verse_index: int = Field(..., title="Verse Index", description="…")
    found: str = Field(..., title="Original Fragment", description="…")
    corrected: str = Field(..., title="Corrected Fragment", description="…")
    position: int = Field(..., title="Position", description="…")