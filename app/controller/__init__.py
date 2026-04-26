from .login_controller import auth_bp
from .menu_controller import menu_bp

all_blueprint = [
    auth_bp,
    menu_bp
]