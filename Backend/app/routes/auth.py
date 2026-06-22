from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.user import RegisterRequest
from app.database.dependencies import get_db
from app.models.user import User
from app.core.security import hash_password

router = APIRouter()