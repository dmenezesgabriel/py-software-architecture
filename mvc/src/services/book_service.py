from src.repositories.book_repository import BookRepository
from src.schemas.book_schema import BookSchema

book_repository = BookRepository()


class BookService:
    def get_all_books(self):
        books = book_repository.get_all_books()
        return [self._instantiate_book_schema(book) for book in books]

    def get_book_by_id(self, book_id):
        book = book_repository.get_book_by_id(book_id)
        return self._instantiate_book_schema(book) if book else None

    def create_book(self, data):
        validated_data = BookSchema(**data)
        book = book_repository.create_book(validated_data.dict())
        return self._instantiate_book_schema(book)

    def update_book(self, book_id, data):
        book = book_repository.get_book_by_id(book_id)
        if book:
            updated_book = book_repository.update_book(book, data)
            return self._instantiate_book_schema(updated_book)

    def delete_book(self, book_id):
        book = book_repository.get_book_by_id(book_id)
        if book:
            book_repository.delete_book(book)

    def _instantiate_book_schema(self, book):
        return BookSchema(
            id=book.id,
            title=book.title,
            author=book.author,
            published_date=book.published_date,
        ).dict()
