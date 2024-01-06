from flask import Blueprint, jsonify, request
from src.repositories.book import BookRepository
from src.services.book import BookService

book_repository = BookRepository()
book_service = BookService(book_repository)
book_api = Blueprint("book", __name__, url_prefix="/api/books/")


@book_api.route("/", methods=["GET"])
def get_books():
    books = book_service.get_all_books()
    return jsonify(books)


@book_api.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = book_service.get_book_by_id(book_id)
    return jsonify(book), 201


@book_api.route("/", methods=["POST"])
def create_book():
    data = request.get_json()
    book = book_service.create_book(data)
    return jsonify(book), 201


@book_api.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    book = book_service.update_book(book_id, data)
    return jsonify(book), 201


@book_api.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book_service.delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"}), 201
