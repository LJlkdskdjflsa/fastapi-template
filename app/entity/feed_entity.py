from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FeedEntity(Base):
    __tablename__ = 'feed'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    type_id = Column(Integer, ForeignKey('feed_type.id'))
    #
    # user = relationship('UserEntity', back_populates='feeds')  # type: ignore
    # feed_type = relationship('FeedTypeEntity', back_populates='feeds')  # type: ignore
    # articles = relationship(ArticleEntity, back_populates='feed')
