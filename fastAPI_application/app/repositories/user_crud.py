from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.crud_repository import CRUD
from core.models.user_model import UserModel


class UserCRUD(CRUD):
    def __init__(self, async_session: AsyncSession):
        super().__init__(async_session)

    async def create(self, user_login: str, user_password: str, user_name: str = None) -> UserModel:
        new_user = UserModel(name=user_name, login=user_login, hash_password=user_password)
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def read(self, user_id: int) -> UserModel | None:
        result = await self.session.execute(select(UserModel).where(UserModel.id == user_id))
        return result.scalars().first()

    async def update(self, **kwargs):
        pass

    async def delete(self, **kwargs):
        pass