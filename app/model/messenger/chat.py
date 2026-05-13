from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, JSON
from typing import List
from core.extensions import db

class Chat(db.Model):
	__tablename__ = 'chats'

	id: Mapped[int] = mapped_column(primary_key=True)
	user_ids: Mapped[List[int]] = mapped_column(JSON, default=list)
