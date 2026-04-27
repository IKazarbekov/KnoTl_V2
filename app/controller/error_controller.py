from flask import Blueprint, redirect

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def handler_404(e):
    '''
    redirect to page menu
    :return: redirect
    '''
    return redirect('/menu')