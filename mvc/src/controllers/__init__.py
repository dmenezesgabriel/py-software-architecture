from flask import Blueprint

from .book_controller import book_blueprint


def register_routes(app):
    app.register_blueprint(book_blueprint)
