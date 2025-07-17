from fastapi import APIRouter, status

from app.api.schemas.user_schemas import UserRead, UserCreate
from app.services.auth_services import Registration

auth_router = APIRouter()


@auth_router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate) -> UserRead | dict:
    new_registration = Registration(user_data)
    return await new_registration.create_new_user()


@auth_router.post("/login")
async def login_user():
    pass


@auth_router.post("/refresh")
async def get_access_token():
    pass


@auth_router.post("/logout")
async def logout_user():
    pass
