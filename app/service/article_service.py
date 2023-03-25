from datetime import datetime

import database
from dto.article_dto import ArticleResult, ArticleInfo
from entity.article_entity import ArticleEntity
from repository.article_repository import ArticleRepository


class ArticleService:
    @staticmethod
    def get_articles() -> list[ArticleResult]:
        article_result = [
            ArticleResult(
                id=1,
                title='Article 1',
                cover_image_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
                type='NFT',
                created_time=datetime(2021, 1, 1, 0, 0, 0),
                tags=['tag1', 'tag2'],
                author_id=1,
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
                source_url='https://www.google.com',
                updated_time=datetime(2021, 1, 1, 0, 0, 0),
            ),

        ]
        # result = ArticleRepository().get_all()

        return article_result

    @staticmethod
    def get_article(article_id: int) -> ArticleResult:
        article_result = ArticleResult(
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
        )
        # result = ArticleRepository().get_by_id(article_id)

        return article_result

    @staticmethod
    @database.transactional()
    def create_article(article_info: ArticleInfo) -> ArticleResult:
        """Create article"""

        # create article entity
        article_entity = ArticleEntity(
            title=article_info.title,
            description=article_info.description,
            cover_image_url=article_info.cover_image_url,
            author_id=article_info.author_id,
            feed_id=article_info.feed_id,
            source_url=article_info.source_url,
            type=article_info.type,
            tags=article_info.tags,
        )

        # save article entity
        result = ArticleRepository().save_one(article_entity)

        # return result dto
        result_dto = ArticleResult(
            id=result.id,
            title=result.title,
            description=result.description,
            cover_image_url=result.cover_image_url,
            author_id=result.author_id,
            feed_id=result.feed_id,
            source_url=result.source_url,
            type=result.type,
            tags=result.tags,
            created_time=result.created_time,
            updated_time=result.updated_time,
        )

        return result_dto
