from __future__ import annotations

import time

from app.models.schemas import Citation, CopilotAskRequest, CopilotAskResponse
from app.services.retrieval import RetrievalService
from app.services.sql_tool import SQLToolService
from app.services.synthesizer import SynthesizerService


class CopilotOrchestrator:
    def __init__(self) -> None:
        self.retrieval = RetrievalService()
        self.sql_tool = SQLToolService()
        self.synthesizer = SynthesizerService()

    def ask(self, req: CopilotAskRequest) -> CopilotAskResponse:
        start = time.perf_counter()

        retrieved = self.retrieval.search(req.question, top_k=req.top_k)
        citations = [
            Citation(source_id=item.source_id, source_type=item.source_type, excerpt=item.excerpt)
            for item in retrieved
        ]

        sql_query, sql_result = self.sql_tool.run_query(req.question)
        answer = self.synthesizer.compose_answer(req.question, citations, sql_result)

        latency_ms = int((time.perf_counter() - start) * 1000)

        return CopilotAskResponse(
            answer=answer,
            citations=citations,
            sql_query=sql_query,
            sql_result=sql_result,
            latency_ms=latency_ms,
            token_usage={"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
        )
