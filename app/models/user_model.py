from pydantic import BaseModel, EmailStr, constr
from datetime import date


class User(BaseModel):
    id: int
    name: constr(max_length=80)
    cpf: constr(min_length=11, max_length=11)
    rg: constr(max_length=20)
    email: str
    address: constr(max_length=120)
    state: constr(max_length=120)
    city: constr(max_length=120)
    birthday: date
    cellphone: constr(max_length=20)
    gender_id: int
    marital_status_id: int
