from app.model.user import User
from app.repository.user_repo import UserRepository

def test_add_and_find_user(app, session):
    real_user = User()
    real_user.login = 'Bob'
    real_user.password = '1234'
    session.add(real_user)
    session.commit()
    user_repo = UserRepository()

    find_user = user_repo.get_by_id(real_user.id)

    assert real_user is not None
    assert real_user.login == find_user.login
    assert real_user.password == find_user.password
    assert real_user.id == find_user.id

def test_find_not_exiting_user(app, session):
    user_repo = UserRepository()

    find_user = user_repo.get_by_id(999)

    assert find_user is None