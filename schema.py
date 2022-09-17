from pydantic import BaseModel
from datetime import datetime

class UserGet(BaseModel):
    id: int
    age: int
    exp_group: int
    gender: int
    source: str
    country: str
    city: str
    os: str
    class Config:
        orm_mode = True

class PostGet(BaseModel):
    id: int
    text: str
    topic: str
    class Config:
        orm_mode = True

class FeedGet(BaseModel):
    user_id: int
    post_id: int
    time: datetime
    action: str
    user: UserGet
    post: PostGet
    class Config:
        orm_mode = True