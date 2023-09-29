from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.routers import main_router

app = FastAPI(
    title='Backend TDD FastAPI',
    description='Backend TDD FastAPI',
    version='0.0.1',
    docs_url='/',
    redoc_url=None,
    license_info={
        'name': 'MIT',
        'url': 'https://opensource.org/licenses/MIT',
    },
    contact={
        'name': 'Walber Vaz',
        'url': 'https://github.com/walber-vaz',
        'email': 'wvs.walber@gmail.com',
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(main_router)  # type: ignore
