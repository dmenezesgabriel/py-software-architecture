from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    published_date: str
