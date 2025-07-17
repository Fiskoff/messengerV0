from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.api.schemas.token_schemas import Token
from app.api.schemas.user_schemas import UserRead, UserCreate
from app.services.auth_services import Registration, Authorization
from app.services.create_jwt import CreateJWT

auth_router = APIRouter()


@auth_router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate) -> UserRead | dict:
    new_registration = Registration(user_data)
    return await new_registration.create_new_user()


@auth_router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    auth_service = Authorization(login=form_data.username,password=form_data.password)
    tokens = await auth_service.authorization()
    if not tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return tokens


@auth_router.post("/refresh", response_model=Token)
async def refresh_access_token(token: Token):
    jwt_creator = CreateJWT()
    payload = jwt_creator.verify_token(token.refresh_token)

    if not payload or payload.get("token_type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )

    new_access_token = jwt_creator.create_access_token({"sub": payload["sub"]})
    new_refresh_token = jwt_creator.create_refresh_token({"sub": payload["sub"]})
    return Token(
        access_token=new_access_token,
        refresh_token=new_refresh_token,
        token_type="bearer"
    )


@auth_router.post("/logout")
async def logout_user():
    pass
