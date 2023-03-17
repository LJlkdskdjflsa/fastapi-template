from datetime import datetime

from dto.article_dto import ArticleResult
from repository.article_repository import ArticleRepository


class ArticleService:
    @staticmethod
    def get_articles() -> list[ArticleResult]:
        result = [
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
                },
                description='Description 1',
            ),
        ]
        result = ArticleRepository().get_all()

        return result
