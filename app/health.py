from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health_check():
    """Simple health-check endpoint"""
    return {"status": "ok", "version": "v1"}
