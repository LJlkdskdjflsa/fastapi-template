from fastapi import APIRouter

from . import article_api

v1_api_router = APIRouter()

# user liability
v1_api_router.include_router(
    article_api.router, prefix='/articles', tags=['articles'],
)
