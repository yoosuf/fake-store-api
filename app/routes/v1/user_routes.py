from flask import Blueprint, request, jsonify
from app.models import User
from app.extensions import db

user_bp = Blueprint('users', __name__)


@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.as_dict() for user in users])


@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.as_dict())


@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' not in data or 'role' not in data or 'email' not in data or 'password' not in data or 'avatar' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_user = User(
        name=data['name'],
        role=data['role'],
        email=data['email'],
        password=data['password'],
        avatar=data['avatar']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.as_dict()), 201


@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    if 'name' not in data and 'role' not in data and 'email' not in data and 'password' not in data and 'avatar' not in data:
        return jsonify({"error": "No fields to update"}), 400

    if 'name' in data:
        user.name = data['name']
    if 'role' in data:
        user.role = data['role']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password = data['password']
    if 'avatar' in data:
        user.avatar = data['avatar']

    db.session.commit()
    return jsonify(user.as_dict())


@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
