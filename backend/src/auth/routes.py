from fastapi import APIRouter, status
from .schemas import User, UserCreateModel


auth_router = APIRouter()


@auth_router.post("/users/register", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreateModel):
    return user_data


@auth_router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
async def get_user_by_id(user_id: str):
    pass
