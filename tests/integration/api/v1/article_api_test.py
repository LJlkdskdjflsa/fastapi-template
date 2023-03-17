from dto.article_dto import ArticleResult


class TestArticleApi:

    def test_get_articles(self, test_client):
        response = test_client.get('v1/articles')

        assert response.status_code == 200

        # parse response to list[ArticleResult]
        articles = response.json()
        for article in articles:
            ArticleResult(**article)
