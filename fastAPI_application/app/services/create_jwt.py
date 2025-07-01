from passlib.context import CryptContext

from core.config import settings


class CreateJWT:
    __SECRET_KEY: str = settings.jwt.secret_key
    __ALGORITHM: str = settings.jwt.algorithm
    __ACCESS_TOKEN_EXPIRE_MINUTES: int = settings.jwt.access_expire
    __REFRESH_TOKEN_EXPIRE_DAYS: int = settings.jwt.refresh_expire

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def create_access_token(self):
        pass

    def create_refresh_token(self):
        pass

    def verify_token(self):
        pass