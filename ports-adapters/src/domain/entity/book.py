from typing import Union

from pydantic import BaseModel


class Book(BaseModel):
    id: Union[int, None] = None
    title: str
    author: str
    published_date: str
