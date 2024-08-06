from flask import Blueprint, jsonify

v1_bp = Blueprint('v1', __name__)


def register_v1_routes(app):
    from .product_routes import product_bp
    from .category_routes import category_bp
    from .user_routes import user_bp
    from .file_routes import file_bp
    from .auth_routes import auth_bp

    v1_bp.register_blueprint(product_bp, url_prefix='/products')
    v1_bp.register_blueprint(category_bp, url_prefix='/categories')
    v1_bp.register_blueprint(user_bp, url_prefix='/users')
    v1_bp.register_blueprint(file_bp, url_prefix='/files')
    v1_bp.register_blueprint(auth_bp, url_prefix='/auth')

    @v1_bp.route('/test', methods=['GET'])
    def test():
        return jsonify({"message": "API v1 is working!"})

    app.register_blueprint(v1_bp, url_prefix='/api/v1')
