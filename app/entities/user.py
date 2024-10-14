from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    rg = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    cellphone = db.Column(db.String(20), nullable=False)

    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
    marital_status_id = db.Column(db.Integer, db.ForeignKey('marital_status.id'), nullable=False)

    def __init__(self, name, cpf, rg, email, address, state, city, birthday, cellphone, gender_id, marital_status_id):
        self.name = name
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.address = address
        self.state = state
        self.city = city
        self.birthday = birthday
        self.cellphone = cellphone
        self.gender_id = gender_id
        self.marital_status_id = marital_status_id
