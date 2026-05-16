from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, JSON
from typing import List
from core.extensions import db

class Chat(db.Model):
	__tablename__ = 'messages'

	id: Mapped[int] = mapped_column(primary_key=True)
	chat_id: Mapped[int] = mapped_column(Integer)
	text: Mapped[str] = mapped_column(String)
