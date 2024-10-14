from pydantic import BaseModel, constr
from datetime import date


class UserUpdate(BaseModel):
    name: constr(max_length=80)
    email: str
    address: constr(max_length=120)
    state: constr(max_length=120)
    city: constr(max_length=120)
    cellphone: constr(max_length=20)
    gender_id: int
    marital_status_id: int
