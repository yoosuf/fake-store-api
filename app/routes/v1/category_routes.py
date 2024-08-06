from flask import Blueprint, request, jsonify
from app.models import Category
from app.extensions import db

category_bp = Blueprint('categories', __name__)


@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.as_dict() for category in categories])


@category_bp.route('/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    return jsonify(category.as_dict())


@category_bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()
    if 'name' not in data or 'image' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    new_category = Category(name=data['name'], image=data['image'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.as_dict()), 201


@category_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()
    if 'name' not in data and 'image' not in data:
        return jsonify({"error": "No fields to update"}), 400
    if 'name' in data:
        category.name = data['name']
    if 'image' in data:
        category.image = data['image']
    db.session.commit()
    return jsonify(category.as_dict())


@category_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return '', 204
