from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from entity.basic_entity import BasicEntity


class FeedEntity(BasicEntity):
    __tablename__ = 'feed'

    url = Column(String(256), nullable=False)
    name = Column(String(64), nullable=False)
    type = Column(String(64), nullable=False)
    user_id = Column(Integer)
    articles: Mapped[List["ArticleEntity"]] = relationship(back_populates="feed")
