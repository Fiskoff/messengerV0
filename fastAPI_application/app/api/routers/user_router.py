from fastapi import APIRouter, HTTPException, status

from app.api.schemas.user_schemas import UserRead, UserCreate
from app.services.user_services import create_new_user


auth_router = APIRouter()


@auth_router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(user_data: UserCreate) -> UserRead:
    return await create_new_user(user_data)
