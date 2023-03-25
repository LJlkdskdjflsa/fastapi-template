from dto.feed_dto import FeedInfo, FeedResult
from entity.feed_entity import FeedEntity
from repository.feed_repository import FeedRepository
from service.feed_service import FeedService


class TestFeedService:

    def test_create_feed(self, monkeypatch):
        # Arrange
        fake_feed_info = FeedInfo(
            url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            name='Feed 1',
            user_id=1,
            type='rss',
        )

        # - fake entity
        fake_feed_entity = FeedEntity(
            id=1,
            url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            name='Feed 1',
            user_id=1,
            type='rss',
            created_time='2021-01-01 00:00:00',
            updated_time='2021-01-01 00:00:00',
        )

        # - monkeypatch repository save_one method
        monkeypatch.setattr(FeedRepository, 'save_one', lambda _, feed_info: fake_feed_entity)

        # Act
        result = FeedService.create_feed(fake_feed_info)

        # Assert
        assert result == FeedResult(
            id=1,
            url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            name='Feed 1',
            user_id=1,
            type='rss',
        )
