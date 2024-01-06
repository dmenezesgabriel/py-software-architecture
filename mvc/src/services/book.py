class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def get_all_books(self):
        books = self.book_repository.get_all_books()
        return [book for book in books]

    def get_book_by_id(self, book_id):
        book = self.book_repository.get_book_by_id(book_id)
        return book if book else None

    def create_book(self, data):
        book = self.book_repository.create_book(data)
        return book

    def update_book(self, book_id, data):
        book = self.book_repository.get_book_by_id(book_id)
        if book:
            updated_book = self.book_repository.update_book(book, data)
            return updated_book

    def delete_book(self, book_id):
        book = self.book_repository.get_book_by_id(book_id)
        if book:
            self.book_repository.delete_book(book)
