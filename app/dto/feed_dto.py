from pydantic import BaseModel


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
