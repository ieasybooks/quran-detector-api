from pydantic import BaseModel, Field


class Correction(BaseModel):
    ayah_index: int = Field(..., title="Ayah Index", description="…")
    original: str = Field(..., title="Original Fragment", description="…")
    corrected: str = Field(..., title="Corrected Fragment", description="…")
    position: int = Field(..., title="Position", description="…")