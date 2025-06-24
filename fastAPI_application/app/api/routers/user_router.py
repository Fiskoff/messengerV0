from fastapi import APIRouter, HTTPException, status

from app.api.schemas.user_schemas import UserRead, UserCreate
from app.services.user_services import create_new_user


auth_router = APIRouter()


@auth_router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Creates a new user account with the provided details",
    responses={
        201: {"description": "User created successfully"},
        400: {"description": "Invalid input or user already exists"},
        500: {"description": "Internal server error"}
    }
)
async def create_user_endpoint(user_data: UserCreate) -> UserRead:
    try:
        return await create_new_user(user_data)
    except ValueError as e:
        # Обработка ошибок валидации/бизнес-логики
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        # Логирование ошибки для администратора
        print(f"Server error when creating user: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user due to server error"
        )