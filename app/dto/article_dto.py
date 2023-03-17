from datetime import datetime

from pydantic import BaseModel


class AuthorResult(BaseModel):
    id: int
    name: str
    photo_url: str


class ArticleResult(BaseModel):
    id: int
    title: str
    description: str
    cover_image_url: str
    type: str
    tags: list[str]
    author: AuthorResult
    created_time: datetime


class ArticleView(BaseModel):
    id: int
    title: str
    description: str
    cover_image_url: str
    type: str
    tags: list[str]
    author: AuthorResult
    created_time: datetime
