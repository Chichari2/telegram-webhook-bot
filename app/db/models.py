from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, index=True)
  title = Column(String, index=True)
  body = Column(String)