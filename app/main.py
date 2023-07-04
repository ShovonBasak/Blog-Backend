
from fastapi import FastAPI

from .database import engine
from app.database import Base
from app.routes import auth, users, posts, votes

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(votes.router)

@app.get('/')
def index():
    return {"message": "Welcome to the world of Python"}
