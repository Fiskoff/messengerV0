from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str | None
    login: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Sergey123",
                "login": "fiskoff123",
                "password": "root123"
            }
        }


class UserCreate(UserSchema):
    pass


class UserRead(UserSchema):
    id: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": 123,
                "name": "Sergey123",
                "login": "fiskoff123",
                "password": "root123"
            }
        }