from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from flask_login import UserMixin
from core.extensions import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped['int'] = mapped_column(primary_key=True)
    name: Mapped['str'] = mapped_column(String(100))
    login: Mapped['str'] = mapped_column(String(100))
    password: Mapped['str'] = mapped_column(String(255))