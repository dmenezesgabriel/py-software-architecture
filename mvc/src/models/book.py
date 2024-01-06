from dataclasses import dataclass

from src import db


@dataclass
class Book(db.Model):
    id: int
    title: str
    author: str
    published_date: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"
