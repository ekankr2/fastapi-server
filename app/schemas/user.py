from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    email: EmailStr
    password: str
