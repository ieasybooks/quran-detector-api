from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Task(str, Enum):
    detect = "detect"
    annotate = "annotate"


class OperationsRequest(BaseModel):
    text: str = Field(..., title="Input Text",
                      description="The Arabic text to process.")
    tasks: list[Task] = Field(...,
                              description="List of operations to perform")
    find_errors: bool = Field(True, title="Find Errors",
                              description="Enable spelling-error detection.")
    find_missing: bool = Field(True, title="Find Missing",
                               description="Enable missing-word detection.")
    allowed_error_percentage: float = Field(0.25, title="Allowed Error %",
                                            ge=0, le=1,
                                            description="Max fraction of words allowed with errors.")
    min_match: int = Field(3, title="Min Match Length",
                           description="Minimum word count for a valid match.")
    return_json: bool = Field(False, title="Return JSON",
                              description="If true, returns match records in structured JSON form.")
    delimiters: Optional[str] = Field(
        None, title="Delimiters",
        description="Custom delimiter regex (defaults to built-in pattern)."
    )
