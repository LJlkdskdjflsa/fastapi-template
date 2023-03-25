from entity.feed_entity import FeedEntity
from repository.basic_repository import BasicRepository


class FeedRepository(BasicRepository[FeedEntity]):
    def __init__(self):
        super().__init__(entity=FeedEntity)
