from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from workout_api.configs.settings import settings

# Criação do engine assíncrono
engine = create_async_engine(settings.DB_URL, echo=False)

# Configuração do sessionmaker utilizando AsyncSession
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Função para obter a sessão de forma assíncrona
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


