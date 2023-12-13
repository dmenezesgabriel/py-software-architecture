from flask import Blueprint, redirect, render_template, request, url_for
from src.repositories.book_repository import BookRepository
from src.services.book_service import BookService

book_repository = BookRepository()
book_service = BookService(book_repository)
book_view = Blueprint('book_app', __name__, url_prefix='/books')


@book_view.route('/')
def index():
    # Fetch all books using the BookService
    books = book_service.get_all_books()
    return render_template('index.html', books=books)


@book_view.route('/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        data = request.form.to_dict()
        # Create a new book using the BookService
        book_service.create_book(data)
        return redirect(url_for('book_app.index'))

    return render_template('create_book.html')


@book_view.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book_details = book_service.get_book_by_id(book_id)

    if request.method == 'POST':
        data = request.form.to_dict()
        # Update the existing book using the BookService
        book_service.update_book(book_id, data)
        return redirect(url_for('book_app.index'))

    return render_template(
        'update_book.html', book_id=book_id, book_details=book_details)


@book_view.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    # Delete the book using the BookService
    book_service.delete_book(book_id)
    return redirect(url_for('book_app.index'))
