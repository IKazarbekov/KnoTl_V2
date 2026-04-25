from idlelib.mainmenu import menudefs

from flask import Flask
from app.controller.login_controller import main_bp as auth_bp
from app.controller.menu_controller import main_bp as menu_bp
from app.model.user import User
from core.extensions import db, login_manager

app = Flask(__name__)

#sessings
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8skwm38sf3w-3j3s8f3ok'

# settings extensions
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# register blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(menu_bp)

# user loader
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

if __name__ == '__main__':
    app.run()