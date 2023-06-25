from typing import List
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import database, schemas

from app.schemas.posts import OutPost
from app.utils.oauth import generate_token


router = APIRouter(
    prefix='',
    tags=['Auth']
)

@router.post('/token', response_model=schemas.Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(database.get_db)):
    return generate_token(form_data, db)
