from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name : str
    email: EmailStr
    phone: str | None = None

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # for ORM -> Pydantic conversion
        