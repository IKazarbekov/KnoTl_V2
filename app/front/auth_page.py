from app.front import page_builder as pb

def login() -> str:
    '''
    login page
    :return: str page
    '''
    return pb.create_page([
        pb.Card('Вход', [
            pb.Form([
                pb.Label('Логин'),
                pb.TextBox('lg'),
                pb.Label('Пароль'),
                pb.TextBox('pw')
            ])
        ])
    ], False)

def register() -> str:
    return pb.create_page([

    ])