from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DetectorSettings(BaseModel):
    find_errors: bool = True
    find_missing: bool = True
    allowed_error_pct: float = Field(default=0.25, ge=0.0, le=1.0)
    min_match: int = Field(default=3, ge=1)
    delimiters: str | None = None


class DetectRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)
    settings: DetectorSettings | None = None


class AnnotateRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)
    settings: DetectorSettings | None = None


class Match(BaseModel):
    surah_name: str
    verses: list[str]
    errors: list[list[Any]]
    start_in_text: int
    end_in_text: int
    aya_start: int
    aya_end: int


class DetectResponse(BaseModel):
    matches: list[Match]


class AnnotateResponse(BaseModel):
    annotated_text: str


class HealthResponse(BaseModel):
    status: str = "ok"
