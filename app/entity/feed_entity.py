from sqlalchemy import Column, Integer, String

from app.entity.mixin.basic_mixin import BasicMixin
from database import Base


class FeedEntity(BasicMixin, Base):
    __tablename__ = 'feed'

    url = Column(String(256), nullable=False)
    name = Column(String(64), nullable=False)
    user_id = Column(Integer)
    type = Column(String(64), nullable=False)
