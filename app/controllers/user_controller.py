from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, Api

from app.models.api_models import define_response_model, define_user_update_model, define_user_post_model, \
    define_user_get_model
from app.models.update_user_model import UserUpdate
from app.services.user_service import UserService
from app.models.response import Response
from sqlalchemy.exc import IntegrityError

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/v1')
api = Api(user_bp, version='1.0', title='User API', description='API de usuários', doc='/swagger')

user_ns = Namespace('users', description='Operações relacionadas a usuários')
api.add_namespace(user_ns)


post_user_model = define_user_post_model(api)
user_model = define_user_get_model(api)
response_model = define_response_model(api, user_model)
update_user_model = define_user_update_model(api)


@user_ns.route("/")
class UserListResource(Resource):

    @api.doc('Retorna todos os usuários')
    @api.param('limit', 'Número de usuários a serem retornados')
    @api.marshal_with(response_model, code=200, description="Usuários encontrados", mask=False)
    @api.response(404, 'Não existem usuários cadastrados')
    @api.response(500, 'Erro ao buscar usuários')
    def get(self):
        """Lista todos os usuários"""
        try:
            limit = request.args.get('limit', type=int)
            users = UserService.get_all_users(limit)
            if not users:
                response = Response(message="Não existem usuários cadastrados", status_code=404, data=None)
                return response.model_dump(), 404
            response = Response(message=f"{len(users)} Usuários encontrados", status_code=200, data=users)
            return response.model_dump(), 200
        except Exception:
            response = Response(message="Erro ao buscar usuários", status_code=500, data=None)
            return response.model_dump(), 500

    @api.expect(post_user_model)
    @api.marshal_with(response_model, code=201, description="Usuário criado com sucesso", mask=False)
    @api.response(500, 'Erro ao criar usuário')
    def post(self):
        """Cria um novo usuário"""
        try:
            data = request.get_json()
            user = UserService.create_user(data)
            user_data = [{key: value for key, value in user.__dict__.items() if key != '_sa_instance_state'}]
            response = Response(message="Usuário criado com sucesso", status_code=201, data=user_data)
            return response.model_dump(), 201
        except IntegrityError:
            response = Response(message="Usuário já cadastrado", status_code=500, data=None)
            return response.model_dump(), 500
        except Exception as e:
            response = Response(message="Erro ao criar usuário", status_code=500, data=None)
            return response.model_dump(), 500


@user_ns.route('/<int:user_id>')
class UserResource(Resource):
    @api.doc('get_user')
    @api.marshal_with(response_model, code=200, description="Usuário encontrado", mask=False)
    @api.response(404, 'Usuário não encontrado')
    @api.response(500, 'Erro ao buscar usuário')
    def get(self, user_id):
        """Busca um usuário pelo ID"""
        try:
            user = UserService.get_user(user_id)
            if user:
                response = Response(message="Usuário encontrado", status_code=200, data=user)
                return response.model_dump(), 200
            response = Response(message="Usuário não encontrado", status_code=404, data=None)
            return response.model_dump(), 404
        except Exception as e:
            response = Response(message="Erro ao buscar usuário", status_code=500, data=None)
            return response.model_dump(), 500

    @api.expect(update_user_model)
    @api.param('user_id', 'ID do usuário')
    @api.response(200, 'Usuário atualizado com sucesso')
    @api.response(404, 'Usuário não encontrado')
    @api.response(500, 'Erro ao atualizar usuário')
    def put(self, user_id):
        """Atualiza um usuário pelo ID"""
        try:
            data = request.get_json()
            updated_user = UserService.update_user(user_id, data)
            if updated_user:
                response = Response(message="Usuário atualizado com sucesso", status_code=200, data=None)
                return response.model_dump(), 200
            response = Response(message="Usuário não encontrado", status_code=404, data=None)
            return response.model_dump(), 404
        except Exception as e:
            response = Response(message="Erro ao atualizar usuário", status_code=500, data=None)
            return response.model_dump(), 500

    @api.doc('delete_user')
    @api.response(200, 'Usuário deletado com sucesso')
    @api.response(404, 'Usuário não encontrado')
    @api.response(500, 'Erro ao deletar usuário')
    def delete(self, user_id):
        """Deleta um usuário pelo ID"""
        try:
            deleted = UserService.delete_user(user_id)
            if deleted:
                response = Response(message="Usuário deletado com sucesso", status_code=200, data=None)
                return response.model_dump(), 200
            response = Response(message="Usuário não encontrado", status_code=404, data=None)
            return response.model_dump(), 404
        except Exception:
            response = Response(message="Erro ao deletar usuário", status_code=500, data=None)
            return response.model_dump(), 500
