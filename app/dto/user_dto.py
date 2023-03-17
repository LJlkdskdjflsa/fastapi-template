from pydantic import BaseModel


class UserViewModel(BaseModel):
    id: int
    user_name: str
    photo_url: str
    user_address: str
    share: dict
    nft: dict
    subscripted_feed_id: list[int]


class UserViewModelForArticle(BaseModel):
    id: int
    user_name: str
    photo_url: str
