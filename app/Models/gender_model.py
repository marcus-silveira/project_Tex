from app import db


class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20), nullable=False, unique=True)
    users = db.relationship('User', backref='gender', lazy=True)

    def __init__(self, description):
        self.description = description
