from fastapi import FastAPI, Depends, HTTPException
from table_user import User
from table_post import Post
from table_feed import Feed
from database import SessionLocal
from sqlalchemy.orm import Session
from schema import UserGet, PostGet, FeedGet
from typing import List


app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db

@app.get('/user/{id}', response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    result = db.query(User).filter(User.id == id).one_or_none()
    if not result:
        raise HTTPException(404, 'Любое сообщение')
    return result

@app.get('/post/{id}', response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    result = db.query(Post).filter(Post.id == id).one_or_none()
    if not result:
        raise HTTPException(404, 'Any message')
    return result


@app.get('/user/{id}/feed', response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    result = db.query(Feed)\
        .filter(Feed.user_id == id)\
        .order_by(Feed.time.desc())\
        .limit(limit)\
        .all()
    return result

@app.get('/post/{id}/feed', response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    result = db.query(Feed)\
        .filter(Feed.post_id == id)\
        .order_by(Feed.time.desc())\
        .limit(limit)\
        .all()
    return result
