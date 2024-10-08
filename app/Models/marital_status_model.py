from app import db


class MaritalStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False, unique=True)
    users = db.relationship('User', backref='marital_status', lazy=True)

    def __init__(self, status):
        self.status = status
