from sqlalchemy import Integer, String, Column, ForeignKey, TIMESTAMP
from database import Base
from table_post import Post
from table_user import User
from sqlalchemy.orm import relationship

class Feed(Base):
    __tablename__ = "feed_action"
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    time = Column(TIMESTAMP)
    action = Column(String)
    user = relationship(User)
    post = relationship(Post)