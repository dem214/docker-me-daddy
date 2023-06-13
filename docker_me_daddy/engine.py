from asyncio import current_task
from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker, create_async_engine, AsyncSession

from .config import settings

engine = create_async_engine(settings.POSTGRES)
session_factory = async_sessionmaker(engine)
Session = async_scoped_session(session_factory, scopefunc=current_task)

async def get_session() -> AsyncSession:
    session = Session()
    yield session
    await Session.remove()

__all__ = [Session, get_session]