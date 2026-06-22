from app.database.database import engine, Base

from app.models.user import User
from app.models.chat import Chat
from app.models.message import Message
from app.models.setting import Setting

Base.metadata.create_all(bind=engine)

print("Database created successfully")