from core.db_helper import db_helper
from app.repositories.user_crud import UserCRUD
from app.api.schemas.user_schemas import UserCreate, UserRead
from app.services.password_manager import PasswordManager
from app.repositories.get_date_user import GetDateUser
from app.services.create_jwt import CreateJWT
from app.api.schemas.token_schemas import Token
from core.models.user_model import UserModel


class Registration:
    def __init__(self, user_data: UserCreate):
        self.name = user_data.name
        self.login = user_data.login
        self.password = user_data.password


    async def check_login(self) -> bool | None:
        async with db_helper.session_factory() as session:
            db_date = GetDateUser(session)
            result = await db_date.get_user_by_login(self.login)

            if result is None:
                return True


    async def create_new_user(self) -> UserRead | dict:
        async with db_helper.session_factory() as session:
            if self.check_login():
                user_crud = UserCRUD(session)
                new_user = await user_crud.create(user_name=self.name, user_login=self.login, user_password=PasswordManager.hash_password(self.password))
                return UserRead(id=new_user.id, name=new_user.name, login=new_user.login)
            else:
                return {"error": "login belongs to another"}


class Authorization:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    async def authorization(self) -> Token | None:
        async with db_helper.session_factory() as session:
            db_data = GetDateUser(session)
            user: UserModel = await db_data.get_user_by_login(self.login)

            if not user:
                return None

            if PasswordManager.verify_password(self.password, user.hash_password):
                jwt_creator = CreateJWT()
                return Token(
                    access_token=jwt_creator.create_access_token({"sub": user.login}),
                    refresh_token=jwt_creator.create_refresh_token({"sub": user.login}),
                    token_type="bearer"
                )
        return None