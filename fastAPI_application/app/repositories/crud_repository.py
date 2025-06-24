from sqlalchemy.ext.asyncio import AsyncSession


class CRUD:
    def __init__(self, async_session: AsyncSession):
        self.session = async_session

    async def create(self, **kwargs):
        pass

    async def read(self, *args):
        pass

    async def update(self, **kwargs):
        pass

    async def delete(self, **kwargs):
        pass