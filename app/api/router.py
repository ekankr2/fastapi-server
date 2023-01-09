from fastapi import APIRouter

from app.api.endpoints import auth, post, user

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(post.router, prefix="/post", tags=["Post"])
