from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend_tdd_fastapi.infra.database import get_session
from backend_tdd_fastapi.modules.user.dto.schemas import (
    UserSchema,
    UserSchemaResponse,
)
from backend_tdd_fastapi.modules.user.model.user_model import User

router = APIRouter()


@router.patch('/{user_id}/', response_model=UserSchemaResponse)
async def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password

    session.commit()
    session.refresh(db_user)

    return db_user
