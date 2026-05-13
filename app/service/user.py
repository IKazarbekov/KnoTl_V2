from app.model.user import User
from core.extensions import repo

def get_by_login(id: int):
    return repo.users.get_by_login(id)
