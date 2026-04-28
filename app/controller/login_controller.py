from flask import Blueprint, request, redirect, url_for
from app.front import auth_page
from flask_login import login_user, logout_user
from app.service import auth as serv

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/')
def root():
    '''
    :return: login and register page
    '''
    return auth_page.get()

@auth_bp.route('/log', methods=['POST'])
def login():
    '''
    login in session
    :return: redirect to menu or to login page
    '''
    args = request.form
    login = args.get('lg')
    password = args.get('pw')
    is_login, error, user = serv.login(login, password)
    if is_login:
        is_button_phone = 'mb' in args
        login_user(user, remember=is_button_phone)
        return redirect(url_for('menu.root'))
    else:
        return auth_page.get(error)


@auth_bp.route('/reg', methods=['POST'])
def registered():
    '''
    :return: redirect to menu or to register page
    '''
    args = request.form
    login = args.get('lg')
    name = args.get('nm')
    password = args.get('pw1')
    is_login, error, user = serv.register(login, password)
    login_user(user)
    return redirect(url_for('menu.root'))

@auth_bp.route('/lgt')
def logout():
    '''logout from user'''
    logout_user()
    return redirect(url_for('.root'))
