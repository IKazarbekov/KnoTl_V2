from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

class Repository:
    def __init__(self):
        self.users = None
        self.tasks = None
        self.chats = None
repo = Repository()
db  = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
