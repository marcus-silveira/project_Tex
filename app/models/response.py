from pydantic import BaseModel


class Response(BaseModel):
    data: list | None
    message: str
    status_code: int

