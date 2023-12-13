from abc import ABC


class BookService(ABC):
    def get_all_books():
        raise NotImplementedError

    def get_book_by_id():
        raise NotImplementedError

    def create_book():
        raise NotImplementedError

    def update_book():
        raise NotImplementedError

    def delete_book():
        raise NotImplementedError




