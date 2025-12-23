from __future__ import annotations

import logging
from contextlib import asynccontextmanager

import quran_detector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, ORJSONResponse
from starlette.requests import Request

from .middleware import BodySizeLimitMiddleware
from .routers.v1 import router as v1_router
from .settings import get_settings


def _configure_logging(level: str) -> None:
    logging.basicConfig(
        level=level.upper(),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


@asynccontextmanager
async def lifespan(_: FastAPI):
    quran_detector.get_engine()
    yield


def create_app() -> FastAPI:
    s = get_settings()
    _configure_logging(s.log_level)

    app = FastAPI(
        title="quran-detector-api",
        version="0.0.1",
        lifespan=lifespan,
        root_path=s.root_path or "",
        default_response_class=ORJSONResponse,
        docs_url="/docs" if s.docs_enabled else None,
        redoc_url="/redoc" if s.docs_enabled else None,
        openapi_url="/openapi.json" if s.docs_enabled else None,
    )

    app.add_middleware(BodySizeLimitMiddleware, max_body_bytes=s.max_body_bytes)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(_: Request, exc: Exception) -> JSONResponse:
        logging.getLogger("quran_detector_api").exception("Unhandled error", exc_info=exc)
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

    origins = s.cors_origins_list()
    if origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    app.include_router(v1_router)
    return app


app = create_app()


def run() -> None:
    import uvicorn

    s = get_settings()
    uvicorn.run(
        "quran_detector_api.main:app",
        host=s.host,
        port=s.port,
        workers=s.workers,
        log_level=s.log_level,
        reload=False,
        factory=False,
    )
