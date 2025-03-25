import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_wallet_info_basic():
    """Базовый тест структуры ответа"""
    response = client.post(
        "/wallet_info",
        params={"address": "TJr3zJnW24eqVyAjNDRoDnwARfhNaAsDaZ"}
    )

    assert response.status_code == 200
    data = response.json()

    required_fields = ["wallet_address", "balance_trx", "bandwidth", "energy"]
    for field in required_fields:
        assert field in data, f"Отсутствует обязательное поле: {field}"


@pytest.mark.asyncio
async def test_wallet_info_error_handling():
    """Тест обработки ошибок"""
    response = client.post("/wallet_info")
    assert response.status_code == 422

    response = client.post(
        "/wallet_info",
        params={"address": "INVALID_ADDRESS"}
    )
    assert response.status_code in [400, 404]
