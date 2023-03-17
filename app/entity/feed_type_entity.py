from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedTypeEntity(Base):
    __tablename__ = 'feed_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    meta = Column(JSON)

    # feeds = relationship(FeedEntity, back_populates='feed_type')
