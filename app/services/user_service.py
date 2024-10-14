from datetime import datetime
from app.repositories.user_repository import UserRepository
from app.entities.user import User
from app.utils import Utils


class UserService:
    @staticmethod
    def get_all_users(limit: int):
        users = UserRepository.get_all(limit)
        
        if not users:
            return None
        return [{key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'} for user in users]

    @staticmethod
    def get_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            return [{key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}]
        return None

    @staticmethod
    def create_user(data):
        Utils.validate_cpf(data['cpf'])
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
        user = UserRepository.create(new_user)
        user_data = {key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}

        return user_data

    @staticmethod
    def update_user(user_id, data):
        if 'birthday' in data:
            try:
                data['birthday'] = datetime.strptime(data['birthday'], '%Y-%m-%d').date()
            except ValueError:
                raise ValueError("Data de nascimento inválida. Formato esperado: YYYY-MM-DD.")

        user = UserRepository.get_by_id(user_id)
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            updated_user = UserRepository.update(user)
            user_data = {key: value for key, value in updated_user.__dict__.items() if key != '_sa_instance_state'}
            return user_data
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            UserRepository.delete(user)
            return True
        return False
