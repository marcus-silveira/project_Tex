from flask_restx import fields


def define_user_post_model(api):
    return api.model('UserPost', {
        'name': fields.String(required=True, description='Nome do usuário'),
        'cpf': fields.String(required=True, description='CPF do usuário'),
        'rg': fields.String(required=True, description='RG do usuário'),
        'email': fields.String(required=True, description='Email do usuário'),
        'address': fields.String(required=True, description='Endereço do usuário'),
        'state': fields.String(required=True, description='Estado do usuário'),
        'city': fields.String(required=True, description='Cidade do usuário'),
        'birthday': fields.String(required=True, description='Data de nascimento do usuário'),
        'cellphone': fields.String(required=True, description='Celular do usuário'),
        'gender_id': fields.Integer(required=True, description='ID do gênero'),
        'marital_status_id': fields.Integer(required=True, description='ID do estado civil')
    })


def define_user_get_model(api):
    return api.model('UserGet', {
        'id': fields.Integer(required=True, description='Id do Usuário'),
        'name': fields.String(required=True, description='Nome do usuário'),
        'cpf': fields.String(required=True, description='CPF do usuário'),
        'rg': fields.String(required=True, description='RG do usuário'),
        'email': fields.String(required=True, description='Email do usuário'),
        'address': fields.String(required=True, description='Endereço do usuário'),
        'state': fields.String(required=True, description='Estado do usuário'),
        'city': fields.String(required=True, description='Cidade do usuário'),
        'birthday': fields.String(required=True, description='Data de nascimento do usuário'),
        'cellphone': fields.String(required=True, description='Celular do usuário'),
        'gender_id': fields.Integer(required=True, description='ID do gênero'),
        'marital_status_id': fields.Integer(required=True, description='ID do estado civil')
    })


def define_user_update_model(api):
    return api.model('UserUpdate', {
        'name': fields.String(required=True, description='Nome do usuário'),
        'email': fields.String(required=True, description='Email do usuário'),
        'address': fields.String(required=True, description='Endereço do usuário'),
        'state': fields.String(required=True, description='Estado do usuário'),
        'city': fields.String(required=True, description='Cidade do usuário'),
        'cellphone': fields.String(required=True, description='Celular do usuário'),
        'gender_id': fields.Integer(required=True, description='ID do gênero'),
        'marital_status_id': fields.Integer(required=True, description='ID do estado civil')
    })


def define_response_model(api, user_model):
    return api.model('Response', {
        'message': fields.String(description='Mensagem de resposta'),
        'status_code': fields.Integer(description='Código de status HTTP'),
        'data': fields.List(fields.Nested(user_model), description='Dados retornados')
    })
