from fastapi import APIRouter, status

from app.api.schemas.user_schemas import UserRead, UserCreate
from app.services.user_services import Registration

auth_router = APIRouter()


@auth_router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(user_data: UserCreate) -> UserRead | dict:
    new_registration = Registration(user_data)
    return await new_registration.create_new_user()

