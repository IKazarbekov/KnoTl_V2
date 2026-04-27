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
from core.extensions import db, login_manager
from app.repository import user_repo
from app.controller import all_blueprint
from app.old.main import old_bp

def create_app(config: str = None) -> Flask:
    '''
    :param config: if is 'testing' then config for test in db sqlite
        else in postgresql
    :return: Flask app
    '''
    app = Flask(__name__)

    # sessings
    if config == 'testing':
        app.config['TESTING'] = True,
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/mydb'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '8skwm38sf3w-3j3s8f3ok'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.permanent_session_lifetime = datetime.timedelta(days=30)

    # settings extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # user loader
    @login_manager.user_loader
    def load_user(user_id):
        return user_repo.get_by_id(user_id)

    #blueprints
    for blueprint in all_blueprint:
        app.register_blueprint(blueprint)
    app.register_blueprint(old_bp, url_prefix = '/old')

    return app