from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.auth.schemas import User, UserCreateModel
from src.auth.service import UserService
from typing import List


auth_router = APIRouter()
user_service = UserService()


@auth_router.post("/register", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    new_user = await user_service.create_user(user_data, session)
    return new_user


@auth_router.get("/{user_uid}", response_model=User)
async def get_user(user_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    print(f"User ID: {user_uid}")
    user = await user_service.get_user_by_id(user_uid, session)
    
    if user:
        return user
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"User not found")


@auth_router.get("/", response_model=List[User])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await user_service.get_all_users(session)
    return users