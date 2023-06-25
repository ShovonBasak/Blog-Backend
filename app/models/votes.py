from tkinter import CASCADE
from sqlalchemy import Column, ForeignKey, Integer
from app.database import Base


class Vote(Base):
    __tablename__ = "votes"

    post_id = Column(Integer, ForeignKey('posts.id', ondelete=CASCADE), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete=CASCADE), primary_key=True)