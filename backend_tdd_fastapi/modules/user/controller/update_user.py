from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend_tdd_fastapi.infra.database import get_session
from backend_tdd_fastapi.modules.user.dto.schemas import (
    UserSchema,
    UserSchemaResponse,
)
from backend_tdd_fastapi.modules.user.model.user_model import User
from backend_tdd_fastapi.security import get_current_user

router = APIRouter()

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.patch('/{user_id}/', response_model=UserSchemaResponse)
async def update_user(
    user_id: int,
    user: UserSchema,
    session: Session,
    current_user: CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You do not have permission to perform this action',
        )

    current_user.username = user.username
    current_user.email = user.email
    current_user.password = user.password

    session.commit()
    session.refresh(current_user)

    return current_user
