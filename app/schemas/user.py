from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    name: Optional[str] = None


# Properties to receive via API on creation
class UserCreateRequest(UserBase):
    email: EmailStr
    password: str
    name: str = Field(..., min_length=1, max_length=30)


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass
