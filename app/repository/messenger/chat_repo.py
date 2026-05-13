from core.extensions import db
from app.model.messenger.chat import Chat

class ChatRepository():
    def __init__(self, db):
        self._db = db

    def create(self, user_ids: list[int]):
        chat = Chat(user_ids = user_ids)

        session = self._db.session
        session.add(chat)
        session.commit()

    def get_all(self, user_id):
        session = self._db.session

        chats = session.query(Chat).filter(Chat.user_ids.contains(user_id)).all()

        return chats
