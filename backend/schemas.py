from pydantic import BaseModel


class WalletResponseSchema(BaseModel):
    wallet_address: str
    balance_trx: float
    bandwidth: int
    energy: int

    class Config:
        from_attributes = True
