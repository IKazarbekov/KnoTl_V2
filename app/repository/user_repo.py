# app/repository/user_repo.py

class UserRepository:
    def __init__(self, db):
        # Одиночное подчеркивание _db — это стандарт для "защищенных" полей в Python
        self._db = db

    def get_by_id(self, user_id):
        from app.model.user import User
        return self._db.session.get(User, user_id)

    def get_by_login(self, login):
        from app.model.user import User
        # Используем современный стиль SQLAlchemy 2.0 через сессию, которую мы передали
        return self._db.session.query(User).filter_by(login=login).first()

    def create(self, login, name, password_hash):
        from app.model.user import User
        user = User(login=login, name=name, password=password_hash)
        self._db.session.add(user)
        self._db.session.commit()
        return user

    def list_all(self):
        from app.model.user import User
        return self._db.session.query(User).all()