import datetime

from . import page_builder as pb

LOGIN = pb.create_page([
    pb.Card("KnoTl", [
        [
            pb.Label("Сайт для кнопочных телефонов"),
            pb.Label("Введите любой логин"),
            pb.Form([
                pb.TextBox("логин", "log"),
                pb.CheckBox("Кнопочный телефон", "kno")
            ], url='/login/guest')
        ]
    ])
],
False)

def main_menu(login: str, button_phone: bool = False):
    return pb.create_page([
        pb.Card("KnoTl", [
                pb.Label(f"Добро пожаловать: {login}", color="blue", size=1),
                pb.Label(f"Время: {datetime.datetime.now().time().strftime("%H:%M")}"),
                pb.Url("Чат", "/chat"),
                pb.Url("Крестики-Нолики", "/ttt"),
                pb.Url("Переводчик", "/lang"),
                pb.Url("Тест(не заходить)", "/test"),
                pb.UrlCard("О сайте", "#a"),
                pb.UrlCard("Что нового", "n"),
                pb.Url("выйти из сессии", "/login/exit"),
        ], id="m"),
        pb.Card("О сайте", [
            pb.Label(f"Сайт для кнопочных телефонов, использует формат wml html, все скрипты происходят на сервере. Наслаждайтесь !"),
            pb.UrlCard("В меню", "#m"),
        ], id="a"),
        pb.Card("Что нового", [
            pb.Label(f"13.04 - Сайт создан, добавлен чат"),
            pb.Label(f"15.04 - Добавлена игра крестики-нолики"),
            pb.Label(f"28.04 - Добавлен переводчик"),
            pb.Label(f"21.04 - Изменение: Чат сохраняет историю"),
            pb.Label(f"22.04 - Добавлена возможность отправки изображений в чат и время в главном меню"),
            pb.UrlCard("В меню", "#m")
        ], id="n")
    ], button_phone)

def chat(messages: list, is_button_phone: bool = False) -> str:
    """
    page main chat for all users
    :param messages: list from page_builder.PageObject
    :param is_button_phone: for optimization for button phones
    :return: page
    """
    return pb.create_page([
        pb.Card("Чат",
                messages +
                [
                    pb.Form([
                        pb.TextBox("Сообщение: ", "mes"),
                        pb.FileBox("file")
                    ])
                ]
            )
    ], is_wml= is_button_phone)

def tictactoe_menu():
    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Крестики-нолики</title>
</head>
<body>
    <h1>Крестики-нолики</h1>
    
    <h3>Создать игру</h3>
    <form action="/ttt/game" method="GET">
        <button type="submit">Создать игру</button>
    </form>
    <br/>
    <br/>
    <br/>
    <form action="/ttt/game" method="GET">
        <label>Логин друга: <input type="text" name="log" placeholder="Логин друга"></label>
        <br><br>
        <button type="submit">Войти к другу</button>
    </form>
</body>
</html>'''

def tictactoe_wait(login: str):
    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ожидание</title>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <h1>Вы создали лобби</h1>
    <h>Дайте другу ваш логин -{login}- для входа к вам</h>
    <form action="/game/exit">
        <button type="submit">Отменить игру</button>
    </form>
</body>
</html>'''

def tictactoe_game(login_enemy: str, map: str, is_step: bool):
    form_send_step = """<form action="/ttt/game">
        <label>Ваш ход: <input type="text" name="step" placeholder="Номер ячейки"></label>
        <button type="submit">Сделать ход</button>
    </form>""" if is_step else ''

    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ожидание</title>
    <meta http-equiv="refresh" content="4">
</head>
<body>
    <h1>Крестики - Нолики</h1>
    <h>Ваш соперник: {login_enemy}</h> <br/>
    {map}
    {form_send_step}
    <br/>
    <form action="/ttt/game">
        <button type="submit">Сдаться</button>
    </form>
</body>
</html>'''

def error_join_game():
    return f'''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Ожидание</title>
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <h1>Нет игрока с таким логином</h1>
        <h>Проверьте логин</h>
    </body>
    </html>'''

def winner_game(winner_string: str):
    return f'''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Конец игры</title>
    </head>
    <body>
        <h1>{winner_string}</h1>
        <form action="/menu">
            <button type="submit">В главное меню</button>
        </form>
    </body>
    </html>'''

def language(is_button_phone: bool, user_word: str, user_frm: str, user_to: str, translate: str = "", error: str = None):
    """

    :param is_button_phone: required for optimization for button phone
    :param user_word: word for translate
    :param user_frm: from language for translate, format: two characters, example en, ru
    :param user_to:  to language for translate, format: two characters, example en, ru
    :param translate: translate word
    :param error: error translation
    :return: html page if is_button_phone is True else wml page
    """
    languages = {"ru":"Русский",
                 "en":"Английский",
                 "ba":"Башкирский"}
    main_card = pb.Card("Переводчик",[
                pb.Content(pb.Label(error, color="red"), not error is None),
                pb.Form([
                    [
                        pb.Label("С этого языка: "),
                        pb.ComboBox("frm", languages, user_frm),
                        pb.TextBox("Текст: ", "txt", default_value=user_word),
                    ],
                    [
                        pb.Label("На этот язык: "),
                        pb.ComboBox("to", languages, user_to),
                        pb.Label("Перевод:" + translate),
                    ]
                ]),
                pb.Url("Назад","/menu")
            ])

    return pb.create_page([main_card], is_wml=is_button_phone)