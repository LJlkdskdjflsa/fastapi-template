import database
from entity.article_entity import ArticleEntity
from entity.feed_entity import FeedEntity
from entity.user_entity import UserEntity
from repository.basic_repository import BasicRepository


class ArticleRepository(BasicRepository[ArticleEntity]):
    def __init__(self):
        super().__init__(entity=ArticleEntity)

    def get_all_with_feed_and_author(self) -> list[ArticleEntity]:
        """Get all articles with feed and author
        join article, feed, author
        by article.feed_id = feed.id
        by article.author_id = author.id
        """

        db_session = next(database.get_db_session())

        result = db_session.query(ArticleEntity) \
            .join(FeedEntity, ArticleEntity.id == FeedEntity.id) \
            .join(UserEntity, ArticleEntity.id == FeedEntity.id) \
            .all()

        return result
