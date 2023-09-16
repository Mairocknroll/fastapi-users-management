from pydantic import BaseModel


class Users(BaseModel):
    name: str
    surname: str
    age: int
    height: int
    weight: int
