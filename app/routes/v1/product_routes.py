from flask import Blueprint, request, jsonify
from app.models import Product, Category
from app.extensions import db

product_bp = Blueprint('products', __name__)


@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products])


@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.as_dict())


@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    if 'title' not in data or 'price' not in data or 'category_id' not in data or 'images' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    if not isinstance(data['images'], list) or not all(isinstance(image, str) for image in data['images']):
        return jsonify({"error": "Images must be a list of strings"}), 400

    category = Category.query.get(data['category_id'])
    if not category:
        return jsonify({"error": "Category not found"}), 404

    new_product = Product(
        title=data['title'],
        price=data['price'],
        description=data.get('description', ''),
        category_id=data['category_id'],
        images=data['images']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.as_dict()), 201


@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    if 'title' not in data and 'price' not in data and 'description' not in data and 'category_id' not in data and 'images' not in data:
        return jsonify({"error": "No fields to update"}), 400

    if 'category_id' in data:
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({"error": "Category not found"}), 404

    if 'title' in data:
        product.title = data['title']
    if 'price' in data:
        product.price = data['price']
    if 'description' in data:
        product.description = data['description']
    if 'category_id' in data:
        product.category_id = data['category_id']
    if 'images' in data:
        if not isinstance(data['images'], list) or not all(isinstance(image, str) for image in data['images']):
            return jsonify({"error": "Images must be a list of strings"}), 400
        product.images = data['images']

    db.session.commit()
    return jsonify(product.as_dict())


@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
