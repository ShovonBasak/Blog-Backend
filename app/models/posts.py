from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text

from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
