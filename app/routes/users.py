from typing import Annotated, List
from typing_extensions import deprecated
from fastapi import Body, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session
from app.utils import oauth

from app.models.users import User
from app.schemas.users import OutUser, CreateUser
from app.database import get_db

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/', response_model=List[OutUser])
def get_users(current_user: Annotated[str, Depends(oauth.get_current_user)], db: Session=Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post('/', response_model=OutUser, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Session=Depends(get_db)):
    user.password = oauth.hash_pass(user.password)
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user
