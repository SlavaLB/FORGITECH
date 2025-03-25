import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.testclient import TestClient

from backend.main import app


@pytest.fixture(scope="session")
def event_loop():
    """Фикстура для создания цикла событий"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def async_db_session():
    """Фикстура асинхронной сессии БД"""
    session = AsyncMock(spec=AsyncSession)
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    yield session
    await session.close()


@pytest.fixture
def test_client():
    """Синхронный TestClient для FastAPI"""
    return TestClient(app)


@pytest.fixture
async def async_client():
    """Асинхронный TestClient с моком запросов"""

    async with AsyncClient(base_url="http://test") as client:
        with patch.object(client, 'get',
                          return_value=MagicMock(status_code=200)):
            yield client


@pytest.fixture
async def mock_async_db_session():
    """Асинхронный мок сессии БД"""
    session = AsyncMock(spec=AsyncSession)
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.close = AsyncMock()
    yield session
    await session.close()


@pytest.fixture
async def mock_wallet_service():
    """Асинхронный мок сервиса кошельков"""
    service = MagicMock()
    service.get_wallet_info = AsyncMock(return_value={
        "wallet_address": "TEST_ADDRESS",
        "balance_trx": 100.0,
        "bandwidth": 500,
        "energy": 200
    })
    yield service
