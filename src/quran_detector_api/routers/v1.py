from __future__ import annotations

import quran_detector
from fastapi import APIRouter, HTTPException
from quran_detector.config import GLOBAL_DELIMITERS
from quran_detector.config import Settings as CoreSettings
from starlette.concurrency import run_in_threadpool

from ..schemas import AnnotateRequest, AnnotateResponse, DetectRequest, DetectResponse, HealthResponse
from ..settings import get_settings

router = APIRouter(prefix="/v1", tags=["v1"])
_DEFAULT_CORE_SETTINGS = CoreSettings()


def _to_core_settings(req_settings) -> CoreSettings:
    if req_settings is None:
        return _DEFAULT_CORE_SETTINGS
    return CoreSettings(
        find_errors=req_settings.find_errors,
        find_missing=req_settings.find_missing,
        allowed_error_pct=req_settings.allowed_error_pct,
        min_match=req_settings.min_match,
        delimiters=req_settings.delimiters or GLOBAL_DELIMITERS,
    )


@router.get("/healthz", response_model=HealthResponse, tags=["health"])
def healthz() -> HealthResponse:
    return HealthResponse()


@router.get("/readyz", response_model=HealthResponse, tags=["health"])
def readyz() -> HealthResponse:
    quran_detector.get_engine()
    return HealthResponse()


@router.post("/detect", response_model=DetectResponse)
async def detect(req: DetectRequest) -> DetectResponse:
    s = get_settings()
    if len(req.text) > s.max_text_length:
        raise HTTPException(status_code=422, detail=f"Text length exceeds {s.max_text_length} characters")
    settings = _to_core_settings(req.settings)
    matches = await run_in_threadpool(quran_detector.detect, req.text, settings)
    return DetectResponse(matches=matches)  # type: ignore[arg-type]


@router.post("/annotate", response_model=AnnotateResponse)
async def annotate(req: AnnotateRequest) -> AnnotateResponse:
    s = get_settings()
    if len(req.text) > s.max_text_length:
        raise HTTPException(status_code=422, detail=f"Text length exceeds {s.max_text_length} characters")
    settings = _to_core_settings(req.settings)
    annotated_text = await run_in_threadpool(quran_detector.annotate, req.text, settings)
    return AnnotateResponse(annotated_text=annotated_text)
