from fastapi import FastAPI

from .routers import router

app = FastAPI(title="Tron Wallet API")

app.include_router(router)
