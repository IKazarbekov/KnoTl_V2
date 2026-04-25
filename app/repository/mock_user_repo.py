from app.model.user import User

class UserRepository:

    def get_by_id(self, user_id):
        if int(user_id) == 1:
            bob = User()
            bob.id = 1
            bob.login = 'Bob'
            return bob
        return None

    def get_by_login(self, login):
        if login == 'Bob':
            bob = User()
            bob.id = 1
            bob.login = 'Bob'
            return bob
        return None

    def create(self, login, password_hash):
        return None

    def list_all(self):
        return None