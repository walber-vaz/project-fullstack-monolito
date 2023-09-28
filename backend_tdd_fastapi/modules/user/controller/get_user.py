from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend_tdd_fastapi.infra.database import get_session
from backend_tdd_fastapi.modules.user.dto.schemas import UserSchemaUserList
from backend_tdd_fastapi.modules.user.model.user_model import User

router = APIRouter()

Session = Annotated[Session, Depends(get_session)]


@router.get('/', response_model=UserSchemaUserList)
async def list_users(
    session: Session,
    skip: int = 0,
    limit: int = 100,
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}
