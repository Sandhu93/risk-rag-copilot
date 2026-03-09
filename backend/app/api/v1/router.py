from app.api.v1.endpoints import copilot, health
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(copilot.router, prefix="/copilot", tags=["copilot"])
