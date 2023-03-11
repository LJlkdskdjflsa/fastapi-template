from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BasicEntity(Base):
    id = Column(Integer, primary_key=True)
