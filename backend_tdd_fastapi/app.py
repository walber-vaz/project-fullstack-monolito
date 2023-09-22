from fastapi import FastAPI

from .routes import main_router

app = FastAPI(
    title='Backend TDD FastAPI',
    description='Backend TDD FastAPI',
    version='0.0.1',
    docs_url='/',
    redoc_url=None,
)

app.include_router(main_router)
