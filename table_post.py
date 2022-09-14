from sqlalchemy import Integer, Column, String
from database import Base, engine, SessionLocal


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = SessionLocal()

    result = (
        session.query(Post)
        .filter(Post.topic == "business")
        .order_by(Post.id.desc())
        .limit(10)
        .all()
    )


    res_id = [result[x].id for x in range(len(result))]
    print(res_id)


