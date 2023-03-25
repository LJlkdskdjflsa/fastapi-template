import database
from dto.user_dto import UserInfo, UserResult
from entity.user_entity import UserEntity
from repository.user_repository import UserRepository


class UserService:

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

    @staticmethod
    @database.transactional()
    def create_user(user_info: UserInfo) -> UserResult:
        """Create users."""

        # create user entity
        user_entity = UserEntity(
            user_name=user_info.user_name,
            photo_url=user_info.photo_url,
            user_address=user_info.user_address,
            share=user_info.share,
            nft=user_info.nft,
            collection=user_info.collection,
        )

        # save user entity
        result = UserRepository().save_one(user_entity)

        # return result dto
        result_dto = UserResult(
            id=result.id,
            user_name=result.user_name,
            photo_url=result.photo_url,
            user_address=result.user_address,
            share=result.share,
            nft=result.nft,
            collection=result.collection,
        )

        return result_dto
