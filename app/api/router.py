from fastapi import APIRouter

from app.api.endpoints import user, post

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["User"])
api_router.include_router(user.router, prefix="/auth", tags=["Auth"])
api_router.include_router(post.router, prefix="/posts", tags=["Post"])
