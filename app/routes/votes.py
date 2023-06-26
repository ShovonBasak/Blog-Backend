from multiprocessing import synchronize
from typing import List

from httpx import delete, get
from sqlalchemy import func, outerjoin
from sqlalchemy.orm import Session

from app import database, models, schemas
from app.utils import oauth
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(
    prefix='/vote',
    tags=['Vote']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def update_vote(vote: schemas.Vote, db: Session = Depends(database.get_db), 
         current_user: models.User = Depends(oauth.get_current_user)):
    
    vote_query = db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, 
                                              models.Vote.user_id==current_user.id)
    found_vote = vote_query.first()

    if vote.direction == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail=f"User {current_user.id} has already voted on this post")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote not found")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "Successfully deleted vote."}
    
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.VoteCount])
def get_votes(db: Session = Depends(database.get_db),
              current_user: models.User = Depends(oauth.get_current_user)):
    result = db.query(models.Post, func.count(models.Vote.post_id).label('votes')
                      ).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True
                             ).group_by(models.Post.id).all()
    return result
