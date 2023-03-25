from dto.user_dto import UserInfo, UserResult
from entity.user_entity import UserEntity
from repository.user_repository import UserRepository
from service.user_service import UserService


class TestUserService:

    def test_create_user(self, monkeypatch):
        # Arrange
        fake_user_info = UserInfo(
            user_name='User 1',
            photo_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            user_address='0x00000000',
            share={},
            nft={},
            collection={},
        )
        # - fake entity
        fake_user_entity = UserEntity(
            id=1,
            user_name='User 1',
            photo_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            user_address='0x00000000',
            share={},
            nft={},
            collection={},
            created_time='2021-01-01 00:00:00',
            updated_time='2021-01-01 00:00:00',
        )

        # - monkeypatch repository save_one method
        monkeypatch.setattr(UserRepository, 'save_one', lambda _, user_info: fake_user_entity)

        # Act

        result = UserService.create_users(fake_user_info)

        # Assert
        assert result == UserResult(
            id=1,
            user_name='User 1',
            photo_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
            user_address='0x00000000',
            share={},
            nft={},
            collection={},
        )
