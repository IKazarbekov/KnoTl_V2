from .login_controller import auth_bp
from .menu_controller import menu_bp
from .error_controller import errors_bp

all_blueprint = [
    auth_bp,
    menu_bp,
    errors_bp
]