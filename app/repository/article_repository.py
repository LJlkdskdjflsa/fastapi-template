from entity.article_entity import ArticleEntity
from repository.basic_repository import BasicRepository


class ArticleRepository(BasicRepository[ArticleEntity]):
    def __init__(self):
        super().__init__(entity=ArticleEntity)
