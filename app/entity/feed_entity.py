from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedEntity(Base):
    __tablename__ = 'feed'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    user_id = Column(Integer)
    type = Column(String)
