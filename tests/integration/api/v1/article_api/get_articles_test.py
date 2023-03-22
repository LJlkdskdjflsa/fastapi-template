from datetime import datetime

from dto.article_dto import ArticleResult, ArticleListView
from repository.article_repository import ArticleRepository


class TestGetArticles:

    def test_get_articles(self, test_client, monkeypatch):
        # monkeypach ArticleRepository.get_all
        def mock_get_all(*args, **kwargs):
            result_a = [
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
                        'support_controller_address': '0x00000000'
                    },
                    feed={
                        'id': 1,
                        'name': 'Feed 1',
                        'photo_url': 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                        'support_controller_address': '0x00000000'
                    },
                    article_url='https://www.google.com',
                    description='Description 1',
                    support_controller_address='0x00000000',
                ),
            ]
            return result_a

        monkeypatch.setattr(ArticleRepository, 'get_all', mock_get_all)

        response = test_client.get('v1/articles')

        assert response.status_code == 200

        # parse response to list[ArticleResult]
        articles = response.json()
        for article in articles:
            ArticleListView(**article)
