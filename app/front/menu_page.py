from app.front.page_builder import *

def start_menu(user_name: str, is_but_mode: bool):
    return create_page([
        Card('KnoTl',[
            Label(f'Привет, {user_name}!'),
            Url('Общий чат', '/old/chat'),
            Url('Крестики Нолики', '/old/ttt'),
            Url('Переводчик', '/old/lang'),
            Label('Новинка !'),
            Url('Задачник', '/todo'),

            Url(f'выйти', '/auth/lgt')
        ])
    ], is_but_mode)
