from sqlalchemy import JSON, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from entity.basic_entity import BasicEntity


class ArticleEntity(BasicEntity):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)
    # author_id = Column(Integer)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["UserEntity"] = relationship(back_populates="articles")
    # feed_id = Column(Integer)
    feed_id: Mapped[int] = mapped_column(ForeignKey("feed.id"))
    feed: Mapped["FeedEntity"] = relationship(back_populates="articles")
    source_url = Column(String(64), nullable=False)
    cover_image_url = Column(String(256), nullable=False)
    type = Column(JSON)
    tags = Column(JSON)
    #
    # author = relationship('UserEntity', back_populates='articles')  # type: ignore
    # feed = relationship('FeedEntity', back_populates='articles')  # type: ignore
