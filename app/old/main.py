from multiprocessing.spawn import old_main_modules

from flask import Blueprint, redirect, request, send_file
from . import game, session, tictactoe
from .front import page
from flask_login import login_required
from .modul import language, chat
from datetime import datetime
import os

# application Flask
old_bp = Blueprint('old_app', __name__)

# chat
@old_bp.route('/chat', methods = ['GET', 'POST'])
@login_required
def rchat():
    args = request.form
    files = request.files
    ip = request.remote_addr
    login, is_but_phone = session.get_log_and_but(ip)

    if 'mes' in args:
        if 'file' in files:
            file = files['file']
            name, ext = os.path.splitext(file.filename)
            path = f"app/old/data/chat/{name}-{datetime.now().strftime("%Y%m%d-%H%M%S")}{ext}"
            file.save(path)
            chat.add_message(login, args['mes'], path)
        else:
            chat.add_message(login, args['mes'])
        return redirect('/old/chat')

    text_messages = chat.get_all_messages()
    return page.chat(text_messages, is_but_phone)

@old_bp.route('/chat/data/<filename>')
@login_required
def chat_data(filename: str):
    ip = request.remote_addr
    if not session.contains(ip):
        return redirect('/login')

    return send_file("../app/old/data/chat/" + filename)

# tic tac toe
@old_bp.route('/ttt')
@login_required
def ttt():
    args = request.args
    ip = request.remote_addr
    if not session.contains(ip):
        return redirect('/login')
    login = session.get_login(ip)

    return page.tictactoe_menu()

# tic tac toe game
@old_bp.route('/ttt/game')
@login_required
def ttt_game():
    args = request.args
    ip = request.remote_addr
    if not session.contains(ip):
        return redirect('/login')
    login = session.get_login(ip)


    # if arg log contains, then this user join in game
    if 'log' in args:
        login_to_user = args['log']
        if game.is_lobby(login_to_user, 'tic-tac-toe'):
            game.remove_lobby(login_to_user, )
            tictactoe.create_game(login, login_to_user)

            game_map = tictactoe.get_map(login)
            is_step = tictactoe.is_step(login)
            return redirect('/ttt/game')
        else:
            return page.error_join_game()

    # if user in game
    if tictactoe.is_in_game(login):
        # if user went
        if 'step' in args:
            step = args['step']
            tictactoe.went(login, step)
            return redirect('/ttt/game')

        # if there is a winner
        winner = tictactoe.who_winner(login)
        if not winner is None:
            return page.winner_game(winner)

        game_map = tictactoe.get_map(login)
        log_enemy = tictactoe.get_enemy(login)
        is_step = tictactoe.is_step(login)
        return page.tictactoe_game(log_enemy, game_map, is_step)

    # if args not, then user create lobby
    game.create_lobby(login, 'tic-tac-toe')

    return page.tictactoe_wait(login)

@old_bp.route('/game/exit')
@login_required
def exit_game():
    pass

@old_bp.route('/lang')
@login_required
def sate_language():
    args = request.args
    ip = request.remote_addr
    if not session.contains(ip):
        return redirect('/login')
    login, is_but_phone = session.get_log_and_but(ip)

    if "txt" in args and "frm" in args and "to" in args:
        user_word = args["txt"]
        from_lang = args["frm"]
        to_lang = args["to"]
        try:
            translate = language.translate_from_api(user_word, from_lang, to_lang)
            return page.language(is_but_phone, user_word, from_lang, to_lang, translate)
        except ConnectionError:
            return page.language(is_but_phone, user_word, from_lang, to_lang, "Ошибка. Попробуйте ещё раз.")

    return page.language(is_but_phone, '', 'ru', 'en')

@old_bp.route('/test')
@login_required
def test_page():
    return """<?xml version="1.0"?>
<!DOCTYPE wml PUBLIC "-//WAPFORUM//DTD WML 1.1//EN" "http://www.wapforum.org/DTD/wml_1.1.xml">

<wml>
    <card id="main" title="Моя страница">
        <p align="center">
            Привет, мир!<br/>
            <a href="#about">О нас</a><br/>
            <a href="tel:+123456789">Позвонить</a>
        </p>
        <input type="file" accept="image/*" capture="camera">
        
        <input type="camera" name="photo" capture="true">
<button>Сфотографировать и отправить</button>

<vibrate pattern="200,100,200">Нажми для вибрации</vibrate>
<button onclick="vibrate(500)">Buzz</button>

<marquee scrollamount="5" behavior="slide" direction="up">Текст ползёт вверх</marquee>

<font face="emoji">😀😎😂</font>
<icon name="battery">🔋</icon>
<icon name="signal">📶</icon>

<postfield name="photo" value="file:///photo.jpg" type="file"/>
    
<input type="capture" name="photo" accept="image/*"/>
<anchor>Снять и отправить
    <go href="upload.cgi" method="post">
        <postfield name="img" value="$(photo)"/>
    </go>
</anchor>

<go href="upload.cgi" method="multipart-post">
    <postfield name="photo" value="$(file:photo.jpg)"/>
</go>

<postfield name="photo" value="$(file:DCIM/photo.jpg)" encoding="base64"/>

<anchor href="data:image/jpeg;base64,/9j/4AAQSkZJRg...">
    Вставить фото из data URI
</anchor>

<input type="file" name="photo" format="image/*" emptyok="false"/>

<go href="upload.cgi" method="post" enctype="multipart/form-data">
    <postfield name="photo" value="$(file:photo.jpg)"/>
</go>

<anchor href="http://server.com/upload.cgi?photo=$(file:photo.jpg:base64)">
    Отправить через GET с base64
</anchor>

<input type="hidden" name="photo" file="DCIM/photo.jpg"/>

    </card>
    
    <card id="about" title="О нас">
        <p>
            Это простая WML-страница.<br/>
            <a href="#main">Назад</a>
        </p>
    </card>
</wml>"""