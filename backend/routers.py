from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import Tron

from .database import get_db
from .models import Wallet
from .schemas import WalletResponseSchema
from .services import WalletInfo, get_wallet_info_service

router = APIRouter()


@router.post("/wallet_info")
async def wallet_info(
        address: str = Query(..., example="TJr3zJnW24eqVyAjNDRoDnwARfhNaAsDaZ"),
        # address: str = Query(..., examples=["TJr3zJnW24eqVyAjNDRoDnwARfhNaAsDaZ",]),
        db: AsyncSession = Depends(get_db),
        wallet_info_service: WalletInfo = Depends(get_wallet_info_service)
):
    tron = Tron(network="nile")
    try:
        account = tron.get_account(address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при получении данных: {str(e)}")

    if not account:
        raise HTTPException(status_code=404, detail="Кошелек не найден")

    wallet_data = await wallet_info_service.get_wallet_info(address)

    new_request = Wallet(
        wallet_address=address,
        balance_trx=wallet_data["balance_trx"],
        bandwidth=wallet_data["bandwidth"],
        energy=wallet_data["energy"],
        created_at=datetime.now(),
    )
    db.add(new_request)
    await db.commit()

    return WalletResponseSchema(
        wallet_address=address,
        balance_trx=wallet_data["balance_trx"],
        bandwidth=wallet_data["bandwidth"],
        energy=wallet_data["energy"],
    )


@router.get("/wallet_requests")
async def get_wallet_requests(
        limit: int = 10,
        offset: int = 0,
        db: AsyncSession = Depends(get_db)
):
    query = select(Wallet).order_by(Wallet.created_at.desc()).limit(limit).offset(offset)
    result = await db.execute(query)
    requests = result.scalars().all()

    return requests
