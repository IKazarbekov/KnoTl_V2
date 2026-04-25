from flask import Blueprint, request, redirect
from app.front import auth_page
#from app.repository.user_repo import UserRepository
from app.repository.mock_user_repo import UserRepository
from flask_login import login_user, logout_user

main_bp = Blueprint('auth', __name__, url_prefix='/auth')
user_repo = UserRepository()

@main_bp.route('/reg')
def register():
    return auth_page.login()

@main_bp.route('/log')
def login():
    args = request.args
    if 'lg' in args:
        login = args['lg']
        user = user_repo.get_by_login(login)
        if user:
            login_user(user)
            return redirect('/menu')
        else:
            return 'not login'

    return auth_page.login()

@main_bp.route('/lgt')
def logout():
    logout_user()
    return redirect('/auth/log')
