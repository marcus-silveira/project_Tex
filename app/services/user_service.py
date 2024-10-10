from app.repositories.user_repository import UserRepository
from app.models.user_model import User


class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def create_user(data):
        user = User(**data)
        return UserRepository.create(user)

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_by_id(user_id)
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            return UserRepository.update(user)
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            UserRepository.delete(user)
            return True
        return False
