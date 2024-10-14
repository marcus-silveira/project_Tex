from app.entities.user import User
from app.entities.marital_status import MaritalStatus
from app.entities.gender import Gender

from app import db, create_app
from flask import redirect

app = create_app()

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return redirect('/api/v1/users/swagger')


if __name__ == '__main__':
    app.run(debug=True)
