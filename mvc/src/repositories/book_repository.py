from src import db
from src.models.book_model import Book


class BookRepository:
    def get_all_books(self):
        return Book.query.all()

    def get_book_by_id(self, book_id):
        return Book.query.get(book_id)

    def create_book(self, data):
        book = Book(**data)
        db.session.add(book)
        db.session.commit()
        return book

    def update_book(self, book, data):
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return book

    def delete_book(self, book):
        db.session.delete(book)
        db.session.commit()
