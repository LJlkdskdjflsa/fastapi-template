from datetime import datetime

from fastapi import APIRouter

from dto.article_dto import ArticleDetailView, ArticleResult, ArticleListView
from service.article_service import ArticleService

router = APIRouter()


@router.post('')
def create_article() -> ArticleDetailView:
    fake_article = ArticleResult(
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
        description='Description 1',
    )
    return fake_article


@router.get('')
def get_articles() -> list[ArticleListView]:
    result_list = ArticleService.get_articles()
    return result_list


@router.get('/{id}')
def get_article(id: int):
    return {'id': id, 'title': 'Article {}'.format(id)}


@router.get('/{id}/status')
def get_article_status(id: int):
    return {'id': id, 'reward_status': 'Not rewarded', 'reward_count': 0, 'reward_amount': 0}
