from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend_tdd_fastapi.infra.database import get_session
from backend_tdd_fastapi.modules.user.dto.schemas import Message
from backend_tdd_fastapi.modules.user.model.user_model import User
from backend_tdd_fastapi.security import get_current_user

router = APIRouter()

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.delete(
    '/{user_id}/',
    response_model=Message,
)
async def delete_user(
    user_id: int,
    session: Session,
    current_user: CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You do not have permission to perform this action',
        )

    session.delete(current_user)
    session.commit()

    return {'detail': 'User deleted'}
