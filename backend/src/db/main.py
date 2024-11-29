from sqlmodel import create_engine, text
from src.config import db_url
from sqlalchemy.ext.asyncio import AsyncEngine


async_engine = AsyncEngine(
    create_engine(
    url = db_url,
    echo = True
)
)

async def init_db():
    async with async_engine.begin() as conn:
        statement = text("SELECT 'hello world';")
        print(statement)
        result = await conn.execute(statement)
        print()
        print(result.all())