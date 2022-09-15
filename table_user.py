from sqlalchemy import Column, String, Integer, func
from database import Base, engine, SessionLocal



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

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = SessionLocal()

    result = session.query(User.country, User.os, func.count(User.id)).filter(User.exp_group == 3).group_by(User.country).group_by(User.os).having(func.count(User.id) > 100).order_by(func.count(User.id).desc()).all()
    print(result)