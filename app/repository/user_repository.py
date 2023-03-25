from entity.user_entity import UserEntity
from repository.basic_repository import BasicRepository


class UserRepository(BasicRepository[UserEntity]):
    def __init__(self):
        super().__init__(entity=UserEntity)
