"""
guest - dict[ip str, (login - str, isButtonPhone - bool)]
"""
from flask import session
from flask_login import current_user
guests = dict()

def add_guest(ip: str, log: str, is_button_phone = False):
    raise Exception()

def contains(ip: str) -> bool:
    return current_user.is_authenticated

def get_login(ip: str) -> str:
    return current_user.login

def is_button_phone(ip: str) -> bool:
    if 'bm' in session:
        return session['bm']
    return False

def get_log_and_but(ip: str) -> tuple[str, bool]:
    return get_login(ip), is_button_phone(ip)

def remove(ip: str):
    raise Exception()