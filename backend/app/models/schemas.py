from typing import Any

from pydantic import BaseModel, Field


class Citation(BaseModel):
    source_id: str
    source_type: str = Field(description="policy|annual_report|table")
    excerpt: str


class CopilotAskRequest(BaseModel):
    question: str = Field(min_length=3)
    user_id: str | None = None
    top_k: int = 5


class CopilotAskResponse(BaseModel):
    answer: str
    citations: list[Citation]
    sql_query: str | None = None
    sql_result: list[dict[str, Any]] | None = None
    latency_ms: int
    token_usage: dict[str, int] | None = None
