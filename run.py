from app import create_app, db
from app.models.user_model import User
from app.models.marital_status_model import MaritalStatus
from app.models.gender_model import Gender

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
