

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
    owner_id: int | None

    class Config:
        orm_mode = True
