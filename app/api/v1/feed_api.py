from fastapi import APIRouter

router = APIRouter()


@router.get('/feeds/{id}')
def get_feeds(id: int):
    return {'data': ['Feed 1', 'Feed 2', 'Feed 3']}


@router.post('/feeds')
def register_feed():
    return {'success': True}


@router.delete('/feeds')
def delete_feed():
    return {'success': True}
