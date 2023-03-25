from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from app.entity.mixin.basic_mixin import BasicMixin

Base = declarative_base()


class FeedEntity(BasicMixin, Base):
    __tablename__ = 'feed'

    id = Column(Integer, primary_key=True)
    url = Column(String(256), nullable=False)
    name = Column(String(64), nullable=False)
    user_id = Column(Integer)
    type = Column(String(64), nullable=False)
