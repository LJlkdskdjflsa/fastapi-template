from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserEntity(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    photo_url = Column(String, nullable=True)
    user_address = Column(String)
    share = Column(JSON)
    nft = Column(JSON)
    subscripted_feed_id = Column(JSON)

    # feeds = relationship(FeedEntity, back_populates='user')
    # articles = relationship(ArticleEntity, back_populates='author')
