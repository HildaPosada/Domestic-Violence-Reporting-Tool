from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import UserCreateModel, UserUpdateModel
from sqlmodel import select, desc
from fastapi.exceptions import HTTPException
from fastapi import status
from .models import User


class UserService:
    
    async def get_user_by_id(self, user_uid: str, session: AsyncSession):
        statement = select(User).where(User.uid == user_uid)

        result = await session.exec(statement)

        user = result.first()

        return user if user is not None else None
    

    async def get_user_by_username(self, username: str, session: AsyncSession):
        statement = select(User).where(User.username == username)

        result = await session.exec(statement)

        user = result.first()

        return user
    
    
    async def user_exists(self, username: str, session: AsyncSession):
        user = await self.get_user_by_username(username, session)

        return True if user is not None else False
      

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):

        user_data_dict = user_data.model_dump()

        existing_user = await self.user_exists(user_data_dict["username"], session)

        if existing_user:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"Choose a another username")

        new_user = User(
            **user_data_dict
        )

        session.add(new_user)

        await session.commit()

        return new_user
    

    async def get_all_users(self, session: AsyncSession):
        statement = select(User).order_by(desc(User.created_at))

        result = await session.exec(statement)

        return result.all()
    

    async def update_user(self, user_uid: str, update_user_data: UserUpdateModel, session: AsyncSession):
        user_to_update = await self.get_user(user_uid, session)

        if user_to_update is not None:
            update_data_dict = update_user_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(user_to_update, k, v)

            await session.commit()

            return user_to_update
        else:
            return None
        

    async def delete_user(self, user_uid: str, session: AsyncSession):

        user_to_delete = await self.get_user(user_uid, session)

        if user_to_delete is not None:
            await session.delete(user_to_delete)

            await session.commit()

            return {}

        else:
            return None