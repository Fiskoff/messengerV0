from core.db_helper import db_helper
from app.repositories.user_crud import UserCRUD
from app.api.schemas.user_schemas import UserCreate, UserRead


async def create_new_user(user_data: UserCreate) -> UserRead:
    async with db_helper.session_factory() as session:
        user_crud = UserCRUD(session)
        new_user = await user_crud.create(user_name=user_data.name, user_login=user_data.login, user_password=user_data.password)
        return UserRead(id=new_user.id, name=new_user.name, login=new_user.login, password=new_user.hash_password)