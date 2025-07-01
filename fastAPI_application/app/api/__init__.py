from fastapi import APIRouter
from app.api.routers.auth_router import auth_router

main_router = APIRouter()
main_router.include_router(auth_router, prefix="/auth", tags=["Auth"])