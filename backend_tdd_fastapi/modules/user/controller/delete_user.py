from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend_tdd_fastapi.infra.database import get_session
from backend_tdd_fastapi.modules.user.dto.schemas import Message
from backend_tdd_fastapi.modules.user.model.user_model import User

router = APIRouter()


@router.delete(
    '/{user_id}/',
    response_model=Message,
)
async def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    session.delete(db_user)
    session.commit()

    return {'detail': 'User deleted'}
