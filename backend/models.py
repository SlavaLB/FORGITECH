from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from .database import Base


class Wallet(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True, nullable=False, unique=False)
    balance_trx = Column(Float, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
