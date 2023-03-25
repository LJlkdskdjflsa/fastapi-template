from sqlalchemy import JSON, Column, String
from sqlalchemy.ext.declarative import declarative_base

from app.entity.mixin.basic_mixin import BasicMixin

Base = declarative_base()


class UserEntity(BasicMixin, Base):
    __tablename__ = 'user'
    user_name = Column(String(64), nullable=False)
    photo_url = Column(String(256), nullable=True)
    user_address = Column(String(256), nullable=False)
    share = Column(JSON)
    nft = Column(JSON)
    collection = Column(JSON)
    # articles: Mapped[List["Article"]] = relationship(back_populates="user")
