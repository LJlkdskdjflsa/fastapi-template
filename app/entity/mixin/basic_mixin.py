from datetime import datetime

from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped, mapped_column


class BasicMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    created_time = Column(Integer, index=True, default=datetime.utcnow().timestamp())
    updated_time = Column(
        Integer, index=True, default=datetime.utcnow().timestamp(),
        onupdate=datetime.utcnow().timestamp(),
    )
