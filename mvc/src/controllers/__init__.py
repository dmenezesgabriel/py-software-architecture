from .book_api import book_api
from .book_view import book_view


def register_routes(app):
    app.register_blueprint(book_api)
    app.register_blueprint(book_view)

