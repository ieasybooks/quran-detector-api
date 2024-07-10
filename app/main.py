from fastapi import FastAPI
from app.health import router as health_router
from app.v1.routers.operations import router as operations_router

app = FastAPI(
    title="Quran Detection API",
    version="v1"
)

app.include_router(health_router, prefix="/api")
app.include_router(operations_router, prefix="/api/v1")