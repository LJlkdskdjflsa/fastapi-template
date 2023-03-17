from datetime import datetime

from pydantic import BaseModel


class ArticleViewModel(BaseModel):
    id: int
    title: str
    feed: dict
    author: dict
    created_time: datetime
