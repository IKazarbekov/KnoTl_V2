from app.model.user import User
from core.extensions import db

class UserRepository:
    def get_by_id(self, user_id):
        return db.session.get(User, user_id)

    def get_by_login(self, login):
        return User.query.filter_by(login=login).first()

    def create(self, login, password_hash):
        user = User(login=login, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    def list_all(self):
        return User.query.all()