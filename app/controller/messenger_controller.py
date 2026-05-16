from flask import Blueprint, session, request, redirect
from flask_login import current_user, login_required
from app.front import messenger_page as page
from app.service.messenger import chat as chat_service
from app.service import user as user_service

msg_bp = Blueprint('msg', __name__, url_prefix='/msg')

@msg_bp.route('/')
@login_required
def root():
    '''
    to show all chat
    '''
    user = current_user
    user_id = user.id

    chats = chat_service.get_user_chats(user_id)

    chat_names_ids = [ ( str(chat.user_ids), chat.id ) for chat in chats]

    return page.list_chats(chat_names_ids)

@msg_bp.route('/new', methods=['POST'])
@login_required
def new_chat():
    '''
    for create new chat
    argument lg: the user login of the user the current one wants to write to
    '''
    args = request.form
    user = current_user

    if 'lg' in args:
        user_id = user.id
        second_user_login = args['lg']
        second_user = user_service.get_by_login(second_user_login)
        second_user_id = second_user.id

        chat_service.create([user_id, second_user_id])

    return redirect('.')

@msg_bp.route('/cnt/<user_login>', methods=['POST'])
@login_required
def new_chat(user_login):
    '''
    for write message
    atgument user_login: the user login of the user the current one wants to write to
    '''
    args = request.form
    user = current_user



    return redirect('.')
