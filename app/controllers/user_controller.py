from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/v1/users')


@user_bp.route("/", methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.__dict__ for user in users])


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user(user_id)
    if user:
        return jsonify([user.__dict__ for user in user])
    return jsonify({'message': 'User not found'}), 404


@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data)
    return jsonify([user.__dict__ for user in user]), 201
