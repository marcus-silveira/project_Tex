from flask_restx import fields

def define_user_model(api):
    return api.model('User', {
        'id': fields.Integer(readOnly=True, description='ID do usuário'),
        'name': fields.String(required=True, description='Nome do usuário'),
        'email': fields.String(required=True, description='Email do usuário')
    })

def define_response_model(api):
    return api.model('Response', {
        'message': fields.String(description='Mensagem de resposta'),
        'status_code': fields.Integer(description='Código de status HTTP'),
        'data': fields.List(fields.Raw, description='Dados retornados')
    })
