import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime

from app.database.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    chat_id = Column(String, ForeignKey("chats.id"))

    role = Column(String)

    content = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)