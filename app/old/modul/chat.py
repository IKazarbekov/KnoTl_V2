import pickle, os
from datetime import datetime
from ..front import page_builder as pb

"""
for work messages in main chat

:dependencies: page_builder, datetime
"""

class Message:
    """
    class for work with messages and save information

    :property file: getter path to file in project
    :property time: getter time in format jour:minute
    :property date: getter date in format year:mount:day
    """
    def __init__(self, user_name: str, text: str, file: str):
        """

        :param user_name: user name which send message
        :param text: text in message
        :param file: path to file in directory data
        """
        self.user_name = user_name
        self.text = text
        self.datetime = datetime.now()
        self.file = file

    @property
    def time(self) -> str:
        return self.datetime.strftime("%H:%M")

    @property
    def date(self) -> str:
        return str(self.datetime.date())

messages = list()
if os.path.exists("app/old/data/chat/chat.bin"):
    with open("app/old/data/chat/chat.bin", "rb") as file:
        messages = pickle.load(file)

# filter words
filter_words = [
    "блядь",
    "пизда",
    "сука",
    "попа",
    "хуй",
    "тварь",
    "ебуч"
]
def text_contains_filter_words(text: str) -> bool:
    """
    :param text: text on check on filter word
    :return: bool
    """
    lower_text = text.lower()
    for word in filter_words:
        if word in lower_text:
            return True
    return False

def add_message(login: str, message: str, file_mes: str = None):
    """
    add message in main chat and filter on bad text and save chat in file
    :param user_name: user name which send message
    :param text: text in message
    :param file: path to file in directory data
    """
    if text_contains_filter_words(message):
        return
    messages.append(Message(login, message, file_mes))
    with open("app/old/data/chat/chat.bin", "wb") as file:
        pickle.dump(messages, file)

def get_all_messages() -> list():
    page_objects = list()
    last_date = None
    for mes in messages:
        # date
        if last_date is None or last_date != mes.date:
            page_objects.append(pb.Label(mes.date, color="green"))
            last_date = mes.date
        # message
        page_object_line = [
            pb.Label(mes.time + "-", color="green"),
            pb.Label(mes.user_name + ":", color="blue"),
            pb.Label(mes.text)
        ]
        page_objects.append(page_object_line)
        # image
        if hasattr(mes, 'file') and not mes.file is None:
            page_objects.append(pb.Image("/old/chat/data/" + os.path.basename(mes.file),
                                         size=100))
    return page_objects