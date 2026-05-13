from app.model.messenger.chat import Chat
from core.extensions import repo

def get_user_chats(user_id: int):
    return repo.chats.get_all(user_id)

def create(user_ids: list[int]):
    repo.chats.create(user_ids)
