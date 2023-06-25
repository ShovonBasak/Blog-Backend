from typing import Type
from pydantic import BaseModel, conint

from app import schemas


class Vote(BaseModel):
    post_id: int
    direction: conint(ge=0, le=1)

class VoteCount(BaseModel):
    Post: schemas.OutPost
    votes: int

    class Config:
        orm_mode = True
