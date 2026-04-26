from flask import Blueprint
from flask_login import current_user, login_required

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('/')
@login_required
def root():
    return f'hello user {current_user}'