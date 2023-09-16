from pydantic import BaseModel

from models.users import Users


class ResResult(BaseModel):
    success: bool
    message: str
    data: list[Users]
