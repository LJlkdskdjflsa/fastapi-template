from sqlalchemy import JSON, Column, Integer, String, Text

from entity.basic_entity import BasicEntity


class ArticleEntity(BasicEntity):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)
    author_id = Column(Integer)
    # author_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    # user: Mapped["User"] = relationship(back_populates="articles")
    feed_id = Column(Integer)
    source_url = Column(String(64), nullable=False)
    cover_image_url = Column(String(256), nullable=False)
    type = Column(JSON)
    tags = Column(JSON)
    #
    # author = relationship('UserEntity', back_populates='articles')  # type: ignore
    # feed = relationship('FeedEntity', back_populates='articles')  # type: ignore
