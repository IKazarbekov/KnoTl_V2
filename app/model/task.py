from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from core.extensions import db

class Task(db.Model):
	__tablename__ = 'tasks'
	
	id: Mapped['int'] = mapped_column(primary_key=True)
	user_id: Mapped['int'] = mapped_column(Integer)
	text: Mapped['str'] = mapped_column(String(100))
	is_completed: Mapped['bool'] = mapped_column(Boolean)
