from fastapi import APIRouter

from dto.article_dto import ArticleView
from service.article_service import ArticleService

router = APIRouter()


@router.get('')
def get_articles() -> list[ArticleView]:
    result_list = ArticleService.get_articles()
    return result_list


@router.get('/{id}')
def get_article(id: int):
    return {'id': id, 'title': 'Article {}'.format(id)}


@router.get('/{id}/status')
def get_article_status(id: int):
    return {'id': id, 'reward_status': 'Not rewarded', 'reward_count': 0, 'reward_amount': 0}
