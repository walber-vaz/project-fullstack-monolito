from fastapi import APIRouter

from api.v1.conf.settings import Settings
from api.v1.modules.auth.controller.generate_token import (
    router as generate_token,
)
from api.v1.modules.user.controller.create_user import router as create_user
from api.v1.modules.user.controller.delete_user import router as delete_user
from api.v1.modules.user.controller.get_user import router as get_user
from api.v1.modules.user.controller.update_user import router as update_user

main_router = APIRouter()

settings = Settings()  # type: ignore

main_router.include_router(
    generate_token, prefix=f'{settings.API_VERSION}', tags=['auth']
)
main_router.include_router(
    create_user, prefix=f'{settings.API_VERSION}/users', tags=['users']
)
main_router.include_router(
    get_user, prefix=f'{settings.API_VERSION}/users', tags=['users']
)
main_router.include_router(
    update_user, prefix=f'{settings.API_VERSION}/users', tags=['users']
)
main_router.include_router(
    delete_user, prefix=f'{settings.API_VERSION}/users', tags=['users']
)
