import time

from app.models.schemas import CopilotAskRequest, CopilotAskResponse
from app.services.orchestrator import CopilotOrchestrator
from fastapi import APIRouter

router = APIRouter()
orchestrator = CopilotOrchestrator()


@router.post("/ask", response_model=CopilotAskResponse)
def ask_copilot(req: CopilotAskRequest) -> CopilotAskResponse:
    t0 = time.perf_counter()
    response = orchestrator.ask(req)
    response.latency_ms = max(response.latency_ms, int((time.perf_counter() - t0) * 1000))
    return response
