from pydantic import AnyUrl, BaseModel


class UserViewModel(BaseModel):
    id: int
    user_name: str
    photo_url: str
    user_address: str
    share: dict
    nft: dict
    subscripted_feed_id: list[int]


class UserResult(BaseModel):
    id: int
    user_name: str
    photo_url: str
    user_address: str
    share: dict
    nft: dict
    collection: dict


class UserViewModelForArticle(BaseModel):
    id: int
    user_name: str
    photo_url: str


class AuthorResult(BaseModel):
    id: int
    name: str
    photo_url: str
    support_controller_address: str


class UserInfo(BaseModel):
    user_name: str
    photo_url: AnyUrl
    user_address: str
    share: dict
    nft: dict
    collection: dict
