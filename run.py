from app import db, create_app
from flask import Flask, redirect, url_for
from app.entities.user_model import User
from app.entities.marital_status_model import MaritalStatus
from app.entities.gender_model import Gender

app = create_app()

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect('/api/v1/users/swagger')

if __name__ == '__main__':
    app.run(debug=True)
