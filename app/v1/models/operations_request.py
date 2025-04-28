from typing import Optional

from pydantic import BaseModel, Field


class OperationsRequest(BaseModel):
    text: str = Field(..., title="Input Text",
        description="The Arabic text to process.")
    tasks: str = Field(..., title="Tasks",
        description="Comma-separated operations: 'detect', 'annotate'.")
    find_errors: bool = Field(True, title="Find Errors",
        description="Enable spelling-error detection.")
    find_missing: bool = Field(True, title="Find Missing",
        description="Enable missing-word detection.")
    allowed_err_pct: float = Field(0.25, title="Allowed Error %",
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