import pytest


@pytest.mark.asyncio
async def test_async_db_session_fixture(mock_async_db_session):
    """Тестируем фикстуру мока асинхронной сессии"""
    await mock_async_db_session.commit()
    await mock_async_db_session.rollback()
    await mock_async_db_session.close()

    mock_async_db_session.commit.assert_awaited_once()
    mock_async_db_session.rollback.assert_awaited_once()
    mock_async_db_session.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_wallet_service_fixture(mock_wallet_service):
    """Тестируем фикстуру сервиса кошельков"""
    result = await mock_wallet_service.get_wallet_info("TEST_ADDRESS")
    assert result["balance_trx"] == 100.0
    mock_wallet_service.get_wallet_info.assert_awaited_once_with(
        "TEST_ADDRESS")


@pytest.mark.asyncio
async def test_async_client_fixture(async_client):
    """Тестируем асинхронный клиент"""
    response = await async_client.get("/path")
    assert response.status_code == 200
