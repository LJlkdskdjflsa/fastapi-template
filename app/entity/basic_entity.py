from datetime import datetime

from sqlalchemy import Integer, text, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BasicEntity(Base):
    __abstract__ = True
    id: int | None = Column(Integer, primary_key=True)
    created_time: datetime = Column(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            'server_default': text('CURRENT_TIMESTAMP'),
        },
    )
    updated_time: datetime = Column(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            'server_default': text('CURRENT_TIMESTAMP'),
            'onupdate': text('CURRENT_TIMESTAMP'),
        },
    )
