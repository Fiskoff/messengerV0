from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user_model import UserModel


class GetDateUser:
    def __init__(self, async_session: AsyncSession):
        self.session = async_session

    async def get_hash_password(self, user_id) -> str | None:
        result = await self.session.execute(select(UserModel).where(UserModel.id == user_id))
        user = result.scalars().first()
        return user.hash_password

    async def get_user_by_login(self, user_login: str) -> str | None:
        result = await self.session.execute(select(UserModel).where(UserModel.login == user_login))
        return result.scalars().first()