from fastapi import APIRouter

from backend_tdd_fastapi.modules.auth.controller.generate_token import (
    router as generate_token,
)
from backend_tdd_fastapi.modules.user.controller.create_user import (
    router as create_user,
)
from backend_tdd_fastapi.modules.user.controller.delete_user import (
    router as delete_user,
)
from backend_tdd_fastapi.modules.user.controller.get_user import (
    router as get_user,
)
from backend_tdd_fastapi.modules.user.controller.update_user import (
    router as update_user,
)

main_router = APIRouter()


main_router.include_router(generate_token, tags=['auth'])
main_router.include_router(create_user, prefix='/users', tags=['users'])
main_router.include_router(get_user, prefix='/users', tags=['users'])
main_router.include_router(update_user, prefix='/users', tags=['users'])
main_router.include_router(delete_user, prefix='/users', tags=['users'])
