

from datetime import datetime
from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr

class CreateUser(BaseUser):
    password: str

class OutUser(BaseUser):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
