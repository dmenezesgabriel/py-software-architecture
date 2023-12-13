from .book_controller import book_api


def register_routes(app):
    app.register_blueprint(book_api)
