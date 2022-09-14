from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    exp_group = Column(Integer)
    gender = Column(Integer)
    source = Column(String)
    country = Column(String)
    city = Column(String)
    os = Column(String)
