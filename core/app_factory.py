'''
for create app Flask with settings
:dependencies:
    flask - for create
    flask login - for setting
    datetime.timedelta - for setting session lifetime
:dependencies in project:
    extensions.db - database from flask_sqlalchemy
    app.repository.user_repo for settings

'''
import datetime
from sys import prefix

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from core.extensions import db, login_manager, migrate, repo
from app.controller import all_blueprint
from app.old.main import old_bp

def create_app(config: str = 'prod') -> Flask:
    '''
    :param config: if is 'testing' then config for test in db sqlite
        else in postgresql
    :return: Flask app
    '''
    app = Flask(__name__)

    # sessings
    if config == 'test_sql_lite':
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        from app.repository.user_repo import UserRepository
        repo.users = UserRepository(db)
    elif config == 'test_mock':
        from app.repository.mock_user_repo import UserMockRepository
        repo.users = UserMockRepository()
    elif config == 'prod':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/mydb'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        from app.repository.user_repo import UserRepository
        repo.users = UserRepository(db)
    else:
        raise ValueError('config error')
    app.config['SECRET_KEY'] = '8skwm38sf3w-3j3s8f3ok'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.permanent_session_lifetime = datetime.timedelta(days=30)

    # settings extensions
    limiter = Limiter(
        key_func = get_remote_address,
        default_limits=['200 per day', '60 per hour']
    )
    limiter.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.root'
    migrate.init_app(app, db)

    # user loader
    @login_manager.user_loader
    def load_user(user_id):
        return repo.users.get_by_id(user_id)

    #blueprints
    for blueprint in all_blueprint:
        app.register_blueprint(blueprint)
    app.register_blueprint(old_bp, url_prefix = '/old')

    return app