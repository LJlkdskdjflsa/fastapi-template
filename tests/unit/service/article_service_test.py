from datetime import datetime

from dto.article_dto import ArticleInfo, ArticleResult
from entity.article_entity import ArticleEntity
from repository.article_repository import ArticleRepository
from service.article_service import ArticleService


class TestArticleService:
    def test_create_article(self, monkeypatch):
        # Arrange
        fake_article_info = ArticleInfo(
            title='Article 1',
            description='Content 1',
            cover_image_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            type='rss',
            tags=['tag1', 'tag2'],
            author_id=1,
            feed_id=1,
            source_url='https://www.google.com',
        )
        # - fake entity
        fake_article_entity = ArticleEntity(
            id=1,
            title='Article 1',
            description='Content 1',
            cover_image_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            type='rss',
            tags=['tag1', 'tag2'],
            author_id=1,
            feed_id=1,
            source_url='https://www.google.com',
            created_time=datetime(2021, 1, 1, 0, 0, 0),
            updated_time=datetime(2021, 1, 1, 0, 0, 0),
        )
        # - monkeypatch repository save_one method

        monkeypatch.setattr(ArticleRepository, 'save_one', lambda _, article_info: fake_article_entity)
        # Act
        result = ArticleService.create_article(fake_article_info)
        # Assert
        assert result == ArticleResult(
            id=1,
            title='Article 1',
            description='Content 1',
            cover_image_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            type='rss',
            tags=['tag1', 'tag2'],
            author_id=1,
            feed_id=1,
            source_url='https://www.google.com',
            created_time=datetime(2021, 1, 1, 0, 0, 0),
            updated_time=datetime(2021, 1, 1, 0, 0, 0),
        )
