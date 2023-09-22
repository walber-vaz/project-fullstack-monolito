from fastapi import APIRouter, HTTPException, status

from backend_tdd_fastapi.modules.user.schemas import (
    Message,
    UserSchema,
    UserSchemaDB,
    UserSchemaResponse,
    UserSchemaUserList,
)

router = APIRouter()
database = []


@router.post(
    '/', status_code=status.HTTP_201_CREATED, response_model=UserSchemaResponse
)
async def create_user(user: UserSchema) -> UserSchemaDB:
    user_with_id = UserSchemaDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@router.get('/', response_model=UserSchemaUserList)
async def list_users() -> dict[str, list[UserSchemaResponse]]:
    return {'users': database}


@router.patch('/{user_id}/', response_model=UserSchemaResponse)
async def update_user(user_id: int, user: UserSchema) -> UserSchemaDB:
    if user_id <= 0 or user_id > len(database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )
    user_with_id = UserSchemaDB(**user.model_dump(), id=user_id)

    database[user_id - 1] = user_with_id

    return user_with_id


@router.delete(
    '/{user_id}/',
    response_model=Message,
)
async def delete_user(user_id: int) -> dict[str, str]:
    try:
        del database[user_id - 1]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    return {'detail': 'User deleted'}
