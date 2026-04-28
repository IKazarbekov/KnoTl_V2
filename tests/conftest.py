import pytest
from core.app_factory import create_app
from core.extensions import db

@pytest.fixture
def app():
    '''
    settings temporary data base on memory
    :return: app flask
    '''
    flask_app = create_app('test_sql_lite')
    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def session():
    '''for direct work with db session'''
    return db.session

@pytest.fixture()
def database():
    return db