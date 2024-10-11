from datetime import datetime
from app.repositories.user_repository import UserRepository
from app.entities.user_model import User


class UserService:
    @staticmethod
    def get_all_users(limit: int):
        users = UserRepository.get_all(limit)
        
        if not users:
            return None
        return [{key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'} for user in users]

    @staticmethod
    def get_user(user_id):
        user =  UserRepository.get_by_id(user_id)
        if user:
            return [{key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}]
        return None

    @staticmethod
    def create_user(data):
        if 'birthday' in data:
            data['birthday'] = datetime.strptime(data['birthday'], '%Y-%m-%d').date()
        
        new_user = User(
            name=data['name'],
            cpf=data['cpf'],
            rg=data['rg'],
            email=data['email'],
            address=data['address'],
            state=data['state'],
            city=data['city'],
            birthday=data['birthday'],
            cellphone=data['cellphone'],
            gender_id=data['gender_id'],
            marital_status_id=data['marital_status_id']
        )
        return UserRepository.create(new_user)

    @staticmethod
    def update_user(user_id, data):
        if 'birthday' in data:
            data['birthday'] = datetime.strptime(data['birthday'], '%Y-%m-%d').date()

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
