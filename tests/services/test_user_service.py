import unittest
from unittest.mock import patch, MagicMock

from app.exceptions.invalid_exception_cpf import InvalidCPFError
from app.services.user_service import UserService
from app.models.user_model import User


class TestUserService(unittest.TestCase):

    @patch('app.services.user_service.UserRepository')
    def test_get_all_users(self, mock_user_repo):
        # Arrange
        mock_user_repo.get_all.return_value = [
            User(id=123, name='Marcus Silveira', cpf='12345678901', rg='MG1234567', email='marcus@example.com',
                 address='123 Main St', state='MG', city='Belo Horizonte', birthday='1990-01-01',
                 cellphone='31987654321', gender_id=1, marital_status_id=1),
            User(id=321, name='Ana Carolina', cpf='12345678902', rg='MG1234568', email='ana@example.com',
                 address='124 Main St', state='MG', city='Belo Horizonte', birthday='1992-01-01',
                 cellphone='31987654322', gender_id=2, marital_status_id=2)
        ]

        # Act
        users = UserService.get_all_users(limit=2)

        # Assert
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0]['name'], 'Marcus Silveira')
        self.assertEqual(users[1]['name'], 'Ana Carolina')
        mock_user_repo.get_all.assert_called_once_with(2)

    @patch('app.services.user_service.UserRepository')
    def test_get_user_success(self, mock_user_repo):
        # Arrange
        mock_user_repo.get_by_id.return_value = User(id=321,name='Marcus Silveira', cpf='12345678901', rg='MG1234567',
                                                     email='marcus@example.com', address='123 Main St',
                                                     state='MG', city='Belo Horizonte',
                                                     birthday='1990-01-01', cellphone='31987654321',
                                                     gender_id=1, marital_status_id=1)

        # Act
        user = UserService.get_user(user_id=1)

        # Assert
        self.assertIsNotNone(user)
        self.assertEqual(user[0]['name'], 'Marcus Silveira')
        self.assertEqual(user[0]['cpf'], '12345678901')
        mock_user_repo.get_by_id.assert_called_once_with(1)

    @patch('app.services.user_service.UserRepository')
    def test_get_user_not_found(self, mock_user_repo):
        # Arrange
        mock_user_repo.get_by_id.return_value = None

        # Act
        user = UserService.get_user(user_id=999)

        # Assert
        self.assertIsNone(user)
        mock_user_repo.get_by_id.assert_called_once_with(999)

    @patch('app.services.user_service.UserRepository')
    def test_create_user_success(self, mock_user_repo):
        # Arrange
        user_data = {
            'name': 'Marcus Silveira',
            'cpf': '60022115005',
            'rg': 'MG1234567',
            'email': 'marcus@example.com',
            'address': '123 Main St',
            'state': 'MG',
            'city': 'Belo Horizonte',
            'birthday': '1990-01-01',
            'cellphone': '31987654321',
            'gender_id': 1,
            'marital_status_id': 1
        }
        mock_user_repo.create.return_value = User(id=178, **user_data)

        # Act
        created_user = UserService.create_user(user_data)

        # Assert
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user["name"], 'Marcus Silveira')
        self.assertEqual(created_user["id"], 178)
        mock_user_repo.create.assert_called_once()

    @patch('app.services.user_service.UserRepository')
    def test_create_user_invalid_cpf(self, mock_user_repo):
        # Arrange
        user_data = {
            'name': 'Marcus Silveira',
            'cpf': '12345678900',  # CPF inválido
            'rg': 'MG1234567',
            'email': 'marcus@example.com',
            'address': '123 Main St',
            'state': 'MG',
            'city': 'Belo Horizonte',
            'birthday': '1990-01-01',
            'cellphone': '31987654321',
            'gender_id': 1,
            'marital_status_id': 1
        }

        # Act & Assert
        with self.assertRaises(InvalidCPFError) as context:
            UserService.create_user(user_data)

        self.assertEqual(str(context.exception), "CPF inválido")

    @patch('app.services.user_service.UserRepository')
    def test_update_user_success(self, mock_user_repo):
        # Arrange
        updated_data = {'name': 'Neymar Jr'}
        mock_user = User(id=321, name='Marcus Silveira', cpf='12345678901',
                         rg='MG1234567', email='marcus@example.com',
                         address='123 Main St', state='MG', city='Belo Horizonte',
                         birthday='1990-01-01', cellphone='31987654321',
                         gender_id=1, marital_status_id=1)

        mock_user_repo.get_by_id.return_value = mock_user
        mock_user_repo.update.return_value = User(**{**mock_user.__dict__, **updated_data})

        # Act
        updated_user = UserService.update_user(321, updated_data)

        # Assert
        self.assertIsNotNone(updated_user)
        print(updated_user)
        self.assertEqual(updated_user["name"], 'Neymar Jr')
        mock_user_repo.get_by_id.assert_called_once_with(321)
        mock_user_repo.update.assert_called_once()

    @patch('app.services.user_service.UserRepository')
    def test_delete_user_success(self, mock_user_repo):
        # Arrange
        mock_user_repo.get_by_id.return_value = User(id=12, name='Marcus Silveira', cpf='12345678901',
                                                     rg='MG1234567', email='marcus@example.com',
                                                     address='123 Main St', state='MG', city='Belo Horizonte',
                                                     birthday='1990-01-01', cellphone='31987654321',
                                                     gender_id=1, marital_status_id=1)

        # Act
        result = UserService.delete_user(12)

        # Assert
        self.assertTrue(result)
        mock_user_repo.get_by_id.assert_called_once_with(12)
        mock_user_repo.delete.assert_called_once()

    @patch('app.services.user_service.UserRepository')
    def test_delete_user_not_found(self, mock_user_repo):
        # Arrange
        user_id = 999
        mock_user_repo.get_by_id.return_value = None

        # Act
        result = UserService.delete_user(user_id)

        # Assert
        self.assertFalse(result)
        mock_user_repo.get_by_id.assert_called_once_with(user_id)


if __name__ == '__main__':
    unittest.main()
