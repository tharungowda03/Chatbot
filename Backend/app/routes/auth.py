from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.auth import get_current_user

from app.database.dependencies import get_db

from app.models.user import User

from app.schemas.user import RegisterRequest
from app.schemas.auth import LoginRequest, TokenResponse

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


# =========================
# REGISTER
# =========================

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    
    existing_user = db.query(User).filter(
        User.email == request.email.lower()
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = hash_password(
        request.password
    )

    new_user = User(
        name=request.name.strip(),
        email=request.email.strip().lower(),
        password_hash=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "email": new_user.email
    }


# =========================
# LOGIN
# =========================

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == request.email.lower()
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    password_valid = verify_password(
        request.password,
        user.password_hash
    )

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": user.id,
            "email": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
@router.get("/me")

def get_me(
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "profile_picture": current_user.profile_picture
    }