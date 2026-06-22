import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime

from app.database.database import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    user_id = Column(String, ForeignKey("users.id"))

    title = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)