from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from fastapi import FastAPI

setup_logging()

app = FastAPI(
    title="RiskRAG Copilot API",
    version="0.1.0",
    description="Starter API for risk/compliance RAG copilot",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "risk-rag-copilot",
        "env": settings.app_env,
        "docs": "/docs",
    }
