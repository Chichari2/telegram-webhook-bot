from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


engine = create_async_engine(settings.POSTGRES_DSN, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)