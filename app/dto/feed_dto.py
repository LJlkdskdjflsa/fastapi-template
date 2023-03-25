from pydantic import BaseModel, AnyUrl


class FeedViewModel(BaseModel):
    id: int
    name: str
    url: str
    user_id: int
    type_id: int


class FeedViewModelForArticle(BaseModel):
    id: int
    name: str
    follow_count: int


class FeedResult(BaseModel):
    id: int
    name: str
    url: AnyUrl
    user_id: int
    type: str


class FeedInfo(BaseModel):
    url: AnyUrl
    name: str
    user_id: int
    type: str
