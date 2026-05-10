from app.front import page_builder as pb

def get(error: str = '') -> str:
    '''
    login page
    :return: str page
    '''
    return pb.create_page([
        pb.Card('Аунтификация',[
            pb.Label(error, color='red'),
            pb.UrlCard('Вход', 'l'),
            pb.UrlCard('Регистрация', 'r')
        ]),
        pb.Card('Вход', [
            pb.Form([
                pb.Label('Логин'),
                pb.TextBox('lg'),
                pb.Label('Пароль'),
                pb.TextBox('pw'),
                [
                    pb.Label('Кнопочный телефон'),
                    pb.CheckBox('bm')
                ]
            ], is_post_method=True, url='log')
        ], id='l'),
        pb.Card('Регистрация', [
            pb.Form([
                pb.Label('Логин'),
                pb.TextBox('lg'),
                pb.Label('Имя'),
                pb.TextBox('nm'),
                pb.Label('Пароль'),
                pb.TextBox('pw1'),
            ], is_post_method=True, url='reg')
        ], id='r')
    ], False)
