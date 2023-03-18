from datetime import datetime

from pydantic import BaseModel


class AuthorResult(BaseModel):
    id: int
    name: str
    photo_url: str
    support_controller_address: str


class FeedResult(BaseModel):
    id: int
    name: str


class ArticleResult(BaseModel):
    id: int
    title: str
    description: str
    cover_image_url: str
    type: str
    tags: list[str]
    author: AuthorResult
    created_time: datetime
    feed: FeedResult
    article_url: str
    support_controller_address: str


class ArticleListView(BaseModel):
    id: int
    title: str
    description: str
    cover_image_url: str
    type: str
    tags: list[str]
    author: AuthorResult
    created_time: datetime


class ArticleDetailView(BaseModel):
    id: int
    author: AuthorResult
    feed: FeedResult
    cover_image_url: str
    title: str
    article_url: str
    support_controller_address: str
    type: str
    tags: list[str]
    created_time: datetime
