from core.extensions import repo
from werkzeug.security import generate_password_hash, check_password_hash
from app.model.user import User

def login(login: str, password: str) -> tuple[bool, str, User]:
    '''
    :param login: user login
    :param password: user password
    :return: tuple[ bool - is_login, str - error, User]
    '''

    user = repo.users.get_by_login(login)
    if user and check_password_hash(user.password, password):
        return True, None, user
    else:
        return False, 'Неверный логин или пароль', None

def register(login: str, name: str, password: str) -> tuple[bool, str, User]:
    '''
    :param login: user login
    :param password: user password
    :return: tuple[bool - is_reg, str - error, User]
    '''
    hash_password = generate_password_hash(password)
    user = repo.users.create(login, name, hash_password)
