from pydantic import BaseModel, Field

from app.v1.models.correction import Correction


class AyahMatch(BaseModel):
    surah_name: str = Field(..., title="Surah Name",
        description="Name of the Surah (chapter) where the ayah is found.")
    surah_number: int = Field(..., title="Surah Number",
        description="Number of the Surah in the Quran.")
    ayah_start: int = Field(..., title="Starting Ayah",
        description="Ayah (ayah) number where the match starts in the Surah.")
    ayah_end: int = Field(..., title="Ending Ayah",
        description="Ayah (ayah) number where the match ends in the Surah.")
    ayah_text: list[str] = Field(..., title="Ayah Text",
        description="Exact text of the ayah(s) matched (normalized).")
    corrections: list[Correction] = Field(..., title="Corrections",
        description="Flat list of all spelling‐error corrections applied.")
    start_index: int = Field(..., title="Start Index",
        description="Character index in the input where this match begins.")
    end_index: int = Field(..., title="End Index",
        description="Character index in the input where this match ends.")