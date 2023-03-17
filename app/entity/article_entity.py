from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ArticleEntity(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    feed_id = Column(Integer, ForeignKey('feed.id'))
    created_time = Column(DateTime)
    source_url = Column(String)
    #
    # author = relationship('UserEntity', back_populates='articles')  # type: ignore
    # feed = relationship('FeedEntity', back_populates='articles')  # type: ignore
