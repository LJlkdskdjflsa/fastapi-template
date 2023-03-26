from fastapi import APIRouter

from dto.article_dto import ArticleDetailView, ArticleListView
from service.article_service import ArticleService

router = APIRouter()


@router.post('')
def create_article() -> ArticleDetailView:
    """Create article (Use for testing)"""
    result = ArticleService.get_articles()
    return result


@router.get('')
def get_articles() -> list[ArticleListView]:
    """Get all articles."""
    result = ArticleService.get_articles()
    return result


@router.get('/{id}')
def get_article(id: int) -> ArticleDetailView:
    """Get article by id."""
    result = ArticleService.get_article(id)
    return result


@router.get('/{id}/status')
def get_article_status(id: int):
    return {'id': id, 'reward_status': 'Not rewarded', 'reward_count': 0, 'reward_amount': 0}
