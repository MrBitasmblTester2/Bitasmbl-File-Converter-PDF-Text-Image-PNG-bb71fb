from fastapi import APIRouter
from .routes import conversion
api_router = APIRouter()
api_router.include_router(conversion.router)
__all__ = ["api_router"]