import uuid
from sqlalchemy import Column, String, DateTime
from datetime import datetime

from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    profile_picture = Column(String, nullable=True)

    google_id = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)