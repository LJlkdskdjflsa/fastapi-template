from repository.article_repository import ArticleRepository


class TestArticleRepository:

    def test_get_all_with_feed_and_author(self):
        # Arrange
        # Act
        result = ArticleRepository().get_all_with_feed_and_author()
        # Assert
        pass
