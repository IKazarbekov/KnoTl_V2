from flask.cli import with_appcontext
from .extensions import db  # или откуда вы берете db
from app.model.user import User    # ваша модель
from werkzeug.security import generate_password_hash

def setup_db_command():
    """Очищает старые данные и создает тестового пользователя."""
    db.drop_all()
    db.create_all()
    
    # Сразу используем правильный хеш, как обсуждали ранее
    test_first_user = User(
        name='Bob', 
        login='bob', 
        password=generate_password_hash('1234')
    )
    test_second_user = User(
        name='Tom',
        login='tom',
        password=generate_password_hash('1234')
    )
    test_three_user = User(
        name='Tom',
        login='tom',
        password=generate_password_hash('1234')
    )
    db.session.add(test_first_user)
    db.session.add(test_second_user)
    db.session.add(test_three_user)
    db.session.commit()
