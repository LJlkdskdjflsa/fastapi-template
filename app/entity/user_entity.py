from typing import List

from sqlalchemy import JSON, Column, String
from sqlalchemy.orm import relationship, Mapped

from entity.basic_entity import BasicEntity


class UserEntity(BasicEntity):
    __tablename__ = 'user'
    user_name = Column(String(64), nullable=False)
    photo_url = Column(String(256), nullable=True)
    user_address = Column(String(256), nullable=False)
    share = Column(JSON)
    nft = Column(JSON)
    collection = Column(JSON)
    articles: Mapped[List["ArticleEntity"]] = relationship(back_populates="author")
