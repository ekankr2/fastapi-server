from fastapi import APIRouter
from fastapi_utils.inferring_router import InferringRouter

from app.api.endpoints import user, post, auth

api_router = APIRouter()

# api_router.include_router(user.router, prefix="/users", tags=["User"])
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
# api_router.include_router(post.router, prefix="/posts", tags=["Post"])
