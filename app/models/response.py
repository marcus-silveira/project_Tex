from pydantic import BaseModel
from datetime import date


class Response(BaseModel):
    data: list | None
    message: str
    status_code: int

    def model_dump(self):
        def serialize_data(data):
            if isinstance(data, list):
                return [serialize_data(item) for item in data]
            if isinstance(data, dict):
                return {key: serialize_data(value) for key, value in data.items()}
            if isinstance(data, date):
                return data.isoformat()
            return data

        return {
            "message": self.message,
            "status_code": self.status_code,
            "data": serialize_data(self.data) if self.data else None
        }
