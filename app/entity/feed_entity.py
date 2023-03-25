from sqlalchemy import Column, Integer, String

from entity.basic_entity import BasicEntity
from database import Base


class FeedEntity(BasicEntity):
    __tablename__ = 'feed'

    url = Column(String(256), nullable=False)
    name = Column(String(64), nullable=False)
    user_id = Column(Integer)
    type = Column(String(64), nullable=False)
