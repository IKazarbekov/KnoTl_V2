from flask import Blueprint, request, redirect, session
from app.front import auth_page
#from app.repository.user_repo import UserRepository
from app.repository import user_repo
from flask_login import login_user, logout_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/reg')
def register():
    return auth_page.login()

@auth_bp.route('/log')
def login():
    args = request.args

    # login code
    if 'lg' in args:
        login = args['lg']
        user = user_repo.get_by_login(login)

        if 'bm' in args:
            session['bm'] = True

        if user:
            login_user(user)
            return redirect('/menu')
        else:
            return 'not login'

    return auth_page.login()

@auth_bp.route('/lgt')
def logout():
    logout_user()
    session.clear()
    return redirect('/auth/log')
