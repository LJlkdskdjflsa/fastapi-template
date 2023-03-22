from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ArticleEntity(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer)
    feed_id = Column(Integer)
    source_url = Column(String)
    #
    # author = relationship('UserEntity', back_populates='articles')  # type: ignore
    # feed = relationship('FeedEntity', back_populates='articles')  # type: ignore
