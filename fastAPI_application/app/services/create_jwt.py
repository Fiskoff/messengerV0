from datetime import datetime, timedelta

from passlib.context import CryptContext
from jwt import encode, decode, PyJWTError

from core.config import settings


class CreateJWT:
    __SECRET_KEY: str = settings.jwt.secret_key
    __ALGORITHM: str = settings.jwt.algorithm
    __ACCESS_TOKEN_EXPIRE_MINUTES: int = settings.jwt.access_expire
    __REFRESH_TOKEN_EXPIRE_DAYS: int = settings.jwt.refresh_expire

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=self.__ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire, "token_type": "access"})
        return encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)

    def create_refresh_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now() + timedelta(days=self.__REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire, "token_type": "refresh"})
        return encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)

    def verify_token(self, token: str) -> dict | None:
        try:
            payload = decode(
                token,
                self.__SECRET_KEY,
                algorithms=[self.__ALGORITHM]
            )
            return payload
        except PyJWTError as error:
            print(error)
            return None