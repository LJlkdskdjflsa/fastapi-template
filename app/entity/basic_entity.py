from datetime import datetime

from sqlalchemy import Integer, Column

from app.database import Base


class BasicEntity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_time = Column(Integer, index=True, default=datetime.utcnow)
    updated_time = Column(Integer, index=True, default=datetime.utcnow, onupdate=datetime.utcnow)
