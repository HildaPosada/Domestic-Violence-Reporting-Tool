from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.auth.routes import auth_router
from src.report.routes import report_router
from src.exception_handler.global_exception import global_exception_handler


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

origins = [
    "http://localhost:5174/",
    "http://localhost:5173/",
    "https://domestic-violence-reporting-tool.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception, global_exception_handler)

@app.get("/")
def root():
    return {"message": "Domestic Violence Reporting Tool"}


app.include_router(auth_router, prefix=f"/api/{version}/users", tags=["users"])

app.include_router(report_router, prefix=f"/api/{version}/reports", tags=["reports"])