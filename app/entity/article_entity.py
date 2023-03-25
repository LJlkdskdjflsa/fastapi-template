from sqlalchemy import Column, Integer, String, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

from app.entity.mixin.basic_mixin import BasicMixin

Base = declarative_base()


class ArticleEntity(BasicMixin, Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)
    author_id = Column(Integer)
    # user: Mapped["User"] = relationship(back_populates="articles")
    feed_id = Column(Integer)
    source_url = Column(String(64), nullable=False)
    cover_image_url = Column(String(256), nullable=False)
    type = Column(JSON)
    tags = Column(JSON)
    #
    # author = relationship('UserEntity', back_populates='articles')  # type: ignore
    # feed = relationship('FeedEntity', back_populates='articles')  # type: ignore
