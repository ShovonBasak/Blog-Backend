

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BasePost(BaseModel):
    title: str
    content: Optional[str]
    published: bool = True

class OutPost(BasePost):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
