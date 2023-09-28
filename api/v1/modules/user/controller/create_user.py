from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from api.security import get_password_hash
from api.v1.infra.database import get_session
from api.v1.modules.user.dto.schemas import UserSchema, UserSchemaResponse
from api.v1.modules.user.model.user_model import User

router = APIRouter()

Session = Annotated[Session, Depends(get_session)]


@router.post(
    '/', status_code=status.HTTP_201_CREATED, response_model=UserSchemaResponse
)
async def create_user(user: UserSchema, session: Session):
    db_user = session.scalar(
        select(User).where(User.username == user.username)
    )

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists',
        )

    db_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user
