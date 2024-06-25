from fastapi import FastAPI
from controller import router as addition_router

app = FastAPI()

app.include_router(addition_router, prefix="/api")
