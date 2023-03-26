from datetime import datetime

import database
from dto.article_dto import ArticleListView, ArticleInfo
from dto.feed_dto import FeedInfo
from dto.user_dto import UserInfo
from service.article_service import ArticleService
from service.feed_service import FeedService
from service.user_service import UserService


class TestGetArticles:

    def test_get_articles(self, test_client, monkeypatch, fake_session):
        # Arrange
        # - use in memory sqlite database
        monkeypatch.setattr(database, 'SessionLocal', fake_session)
        # - create fake data
        #   - create fake user
        fake_user_info = UserInfo(
            user_name='User 1',
            photo_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            user_address='0x00000000',
            share={},
            nft={},
            collection={},
        )
        UserService.create_user(user_info=fake_user_info)

        #   - create fake feed

        fake_feed_info = FeedInfo(
            url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            name='Feed 1',
            user_id=1,
            type='rss',
        )
        FeedService.create_feed(feed_info=fake_feed_info)

        #   - create fake article

        fake_article_info = ArticleInfo(
            title='Article 1',
            description='Article 1 description',
            cover_image_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            type='rss',
            tags=['tag1', 'tag2'],
            author_id=1,
            feed_id=1,
            source_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            created_time=datetime.now(),
            updated_time=datetime.now(),
        )
        ArticleService.create_article(article_info=fake_article_info)

        # Act
        response = test_client.get('v1/articles')

        # Assert
        assert response.status_code == 200

        # parse response to list[ArticleResult]
        articles = response.json()
        for article in articles:
            ArticleListView(**article)
