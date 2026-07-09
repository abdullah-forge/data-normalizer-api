from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncSession
from typing import AsyncGenerator
from app.config.settings import settings

engine = create_async_engine(settings.database_url,echo= settings.database_echo)

async_session = async_sessionmaker(
    bind = engine,
    expire_on_commit = False,
    class_ = AsyncSession
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
         yield session
        
