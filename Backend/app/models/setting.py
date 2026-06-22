import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey

from app.database.database import Base

class Setting(Base):
    __tablename__ = "settings"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    user_id = Column(String, ForeignKey("users.id"))

    voice_enabled = Column(Boolean, default=False)