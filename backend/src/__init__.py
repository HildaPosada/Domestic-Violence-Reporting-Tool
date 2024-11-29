from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting....")
    await init_db()
    yield
    print(f"Server has stopped Stopped")

version = "v1"

app = FastAPI(
    title="Domestic Violence Reporting Tool API",
    description="This is a backend for the Domestic Violence Reporting Tool project",
    version=version,
    lifespan=life_span
)

@app.get("/")
async def index():
    return {"message": "hello world"}