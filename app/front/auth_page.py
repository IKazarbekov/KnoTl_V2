from app.front import page_builder as pb

def login():
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