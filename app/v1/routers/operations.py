from fastapi import APIRouter, HTTPException, status

from app.v1.models.operations_request import OperationsRequest
from app.v1.models.operations_response import OperationsResponse
router = APIRouter()


@router.post("/operations", response_model=OperationsResponse, tags=["Operations"])
async def operations(request: OperationsRequest):
    """Stub: validate request and return a dummy response"""
    # TODO: integrate QuranMatcher logic here

    return OperationsResponse(
        text=request.text,
        matches=[]
    )
