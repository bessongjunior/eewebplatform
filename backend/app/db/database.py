from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import config

SQLITE_URI = 'sqlite:///./app/apidata.db'
POSTGRESQL_URI = f'postgresql+asyncpg://{config.DATABASE_USERNAME}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOSTNAME}:{config.DATABASE_PORT}/{config.DATABASE_NAME}'

if (config.debugging):
    engine = create_async_engine(SQLITE_URI, future=True, echo=True, connect_args={'check_same_thread': False})#create_engine(SQLITE_URI, connect_args={'check_same_thread': False})
else:
    engine = create_async_engine(POSTGRESQL_URI, future=True, echo=True) #create_engine(POSTGRESQL_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False, class_=AsyncSession)()
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def commit_rollback():
    db = SessionLocal()
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
