from fastapi import APIRouter

router = APIRouter()


@router.get('/users/{id}')
def get_user(id: int):
    return {'id': id, 'name': 'User {}'.format(id), 'address': '123 Main St'}


@router.put('/users/{id}')
def update_user(id: int, user_info: dict):
    return {'id': id, 'success': True}
