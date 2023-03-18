from datetime import datetime

from sqlalchemy import Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BasicEntity(Base):
    __abstract__ = True
    id: int | None = Column(Integer, primary_key=True)
    created_time: datetime = Column(
        default=datetime.utcnow,
        nullable=False,
    )
    updated_time: datetime = Column(
        default=datetime.utcnow,
        nullable=False,
    )
