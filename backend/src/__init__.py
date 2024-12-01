from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.auth.routes import auth_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting....")
    await init_db()
    yield
    print(f"Server has stopped.")

version = "v1"

app = FastAPI(
    title="Domestic Violence Reporting Tool API",
    description="This is a backend for the Domestic Violence Reporting Tool project",
    version=version,
    lifespan=life_span
)

@app.get("/")
def root():
    return {"message": "Domestic Violence Reporting Tool"}


app.include_router(auth_router, prefix=f"/api/{version}/users", tags=["users"])