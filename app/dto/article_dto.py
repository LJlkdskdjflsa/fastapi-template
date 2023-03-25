from datetime import datetime

from pydantic import BaseModel, AnyUrl

from dto.feed_dto import FeedResult
from dto.user_dto import AuthorResult


class ArticleResult(BaseModel):
    id: int
    title: str
    description: str
    cover_image_url: AnyUrl
    type: str
    tags: list[str]
    # author: AuthorResult
    author_id: int
    # feed: FeedResult
    source_url: AnyUrl
    created_time: datetime
    updated_time: datetime
    # support_controller_address: str


class ArticleListView(BaseModel):
    id: int
    title: str
    description: str
    cover_image_url: AnyUrl
    type: str
    tags: list[str]
    # author: AuthorResult
    created_time: datetime


class ArticleInfo(BaseModel):
    title: str
    description: str
    cover_image_url: str
    type: str
    tags: list[str]
    author_id: int
    feed_id: int
    source_url: AnyUrl


class ArticleDetailView(BaseModel):
    id: int
    author: AuthorResult
    feed: FeedResult
    cover_image_url: AnyUrl
    title: str
    article_url: AnyUrl
    support_controller_address: str
    type: str
    tags: list[str]
    created_time: datetime
