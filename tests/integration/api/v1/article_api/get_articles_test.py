from datetime import datetime

import database
from dto.article_dto import ArticleListView, ArticleResult
from dto.feed_dto import FeedInfo
from dto.user_dto import UserInfo
from repository.article_repository import ArticleRepository
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
        result = FeedService.create_feed(feed_info=fake_feed_info)

        #   - create fake article

        def mock_get_all(*args, **kwargs):
            fake_result = [
                ArticleResult(
                    id=1,
                    title='Article 1',
                    cover_image_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                    type='NFT',
                    created_time=datetime(2021, 1, 1, 0, 0, 0),
                    tags=['tag1', 'tag2'],
                    author={
                        'id': 1,
                        'name': 'Author 1',
                        'photo_url': 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                        'support_controller_address': '0x00000000',
                    },
                    feed={
                        'id': 1,
                        'name': 'Feed 1',
                        'photo_url': 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                        'support_controller_address': '0x00000000',
                    },
                    article_url='https://www.google.com',
                    description='Description 1',
                    support_controller_address='0x00000000',
                ),
            ]
            return fake_result

        monkeypatch.setattr(ArticleRepository, 'get_all', mock_get_all)

        # Act
        response = test_client.get('v1/articles')

        # Assert
        assert response.status_code == 200

        # parse response to list[ArticleResult]
        articles = response.json()
        for article in articles:
            ArticleListView(**article)
