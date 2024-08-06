def register_routes(app):
    from app.routes.v1 import register_v1_routes
    register_v1_routes(app)