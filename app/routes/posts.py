from typing import List, Annotated
from fastapi import Body, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy.orm import Session

from app.models.posts import Post
from app.schemas.posts import OutPost, BasePost
from app import database
from app.utils.oauth import get_current_user

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('/', response_model=List[OutPost])
def get_posts(user: Annotated[str, Depends(get_current_user)], db: Session=Depends(database.get_db)):
    posts = db.query(Post).all()
    return posts


@router.get('/{id}', response_model=OutPost)
def get_post(id: int, user: Annotated[str, Depends(get_current_user)], db: Session=Depends(database.get_db)):
    print(user)
    post = db.query(Post).get({'id': id})
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OutPost)
def create_post(post: BasePost, user: Annotated[str, Depends(get_current_user)], db: Session=Depends(database.get_db)):
    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, user: Annotated[str, Depends(get_current_user)], db: Session=Depends(database.get_db)):
    post = db.query(Post).get({'id': id})
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=OutPost)
def update_post(id: int, updated_post: BasePost, user: Annotated[str, Depends(get_current_user)], db: Session=Depends(database.get_db)):
    post_query = db.query(Post).filter(Post.id==id)
    post = post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()