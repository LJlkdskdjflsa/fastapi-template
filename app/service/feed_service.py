import database
from dto.feed_dto import FeedInfo, FeedResult
from entity.feed_entity import FeedEntity
from repository.feed_repository import FeedRepository


class FeedService:
    """Feed Service"""

    @staticmethod
    @database.transactional()
    def create_feed(feed_info: FeedInfo) -> FeedResult:
        """Create feed."""

        # create feed entity
        feed_entity = FeedEntity(
            url=feed_info.url,
            name=feed_info.name,
            user_id=feed_info.user_id,
            type=feed_info.type,
        )

        # save feed entity
        result = FeedRepository().save_one(feed_entity)

        # return result dto as FeedResult
        result_dto = FeedResult(
            id=result.id,
            url=result.url,
            name=result.name,
            user_id=result.user_id,
            type=result.type,
        )

        return result_dto
