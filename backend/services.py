from typing import Any, Dict

from fastapi import HTTPException
from tronpy import Tron


class WalletInfo:
    def __init__(self, network: str = "nile"):
        self.tron = Tron(network=network)

    async def get_wallet_info(self, address: str) -> Dict[str, Any]:
        """
        Метод для получения информации о кошельке по адресу
        Возвращает баланс, bandwidth и energy для указанного адреса кошелька
        """

        try:
            account = self.tron.get_account(address)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Ошибка при получении данных: {str(e)}")

        if not account:
            raise HTTPException(status_code=404, detail="Кошелек не найден")

        balance = account.get("balance", 0)
        bandwidth = account.get("bandwidth", 0)
        energy = account.get("energy", 0)

        return {
            "balance_trx": balance,
            "bandwidth": bandwidth,
            "energy": energy
        }


def get_wallet_info_service() -> WalletInfo:
    return WalletInfo(network="nile")
