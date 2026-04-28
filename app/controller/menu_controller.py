from flask import Blueprint, session
from flask_login import current_user, login_required
from app.front.menu_page import start_menu

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')

@menu_bp.route('/')
@login_required
def root():
    is_but_mode = False
    if 'bm' in session:
        is_but_mode = session['bm']
    return start_menu(current_user.name, is_but_mode)