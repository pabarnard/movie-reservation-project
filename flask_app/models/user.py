from flask_app import db
from sqlalchemy import Uuid, String, Integer, DateTime, select, update, delete, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
import uuid, datetime

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    birthdate: Mapped[Date] = mapped_column(Date, nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(511), nullable=False)
    admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    # Relationships will be added here

