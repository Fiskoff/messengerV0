from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str | None
    login: str


class UserRead(UserSchema):
    id: int

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Sergey123",
                "login": "fiskoff123",
                "id": 123,
            }
        }


class UserCreate(BaseModel):
    name: str | None
    login: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Sergey123 | None",
                "login": "fiskoff123",
                "password": "root123",
            }
        }