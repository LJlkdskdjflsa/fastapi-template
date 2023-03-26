import database
from dto.article_dto import ArticleInfo, ArticleResult, ArticleDetailResult
from entity.article_entity import ArticleEntity
from repository.article_repository import ArticleRepository


class ArticleService:
    @staticmethod
    def get_articles() -> list[ArticleResult]:
        """Get all articles."""

        # get all article entities
        result = ArticleRepository().get_all()

        # return result dto
        result_dto = [
            ArticleResult(
                id=article.id,
                title=article.title,
                description=article.description,
                cover_image_url=article.cover_image_url,
                type=article.type,
                tags=article.tags,
                author_id=article.author_id,
                feed_id=article.feed_id,
                source_url=article.source_url,
                created_time=article.created_time,
                updated_time=article.updated_time,
            )
            for article in result
        ]

        return result_dto

    @staticmethod
    def get_article(article_id: int) -> ArticleResult:
        # get article entity
        result = ArticleRepository().get_one_by_id(article_id)

        # return result dto
        result_dto = ArticleResult(
            id=result.id,
            title=result.title,
            description=result.description,
            cover_image_url=result.cover_image_url,
            type=result.type,
            tags=result.tags,
            author_id=result.author_id,
            feed_id=result.feed_id,
            source_url=result.source_url,
            created_time=result.created_time,
            updated_time=result.updated_time,
        )

        return result_dto

    @staticmethod
    def get_article_detail(article_id: int) -> ArticleDetailResult:
        """Get article detail"""
        pass

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
