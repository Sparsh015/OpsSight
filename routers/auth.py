from fastapi import Depends, HTTPException, APIRouter
from app.database import SessionLocal
from models import User
from schemas.user import UserLogin, UserSignup, UserResponse
from auth.security import get_password_hash, verify_password
from auth.token import create_access_token, get_current_user
from fastapi import Depends


router = APIRouter()

@router.post("/signup", response_model=UserResponse)
def signup(user : UserSignup):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code= 400,
            detail = "already registered email"
        )

    hashed_password = get_password_hash(user.password)
    new_user = User(
        username = user.username,
        email = user.email,
        password_hash = hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(user : UserLogin):
    db = SessionLocal()
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user :
        raise HTTPException(
            status_code= 401,
            detail = "user not found. Signup first."
        )
    
    if not verify_password(
        user.password, 
        existing_user.password_hash
    ):
        raise HTTPException(
            status_code= 401,
            detail = "wrong password"
        )
    
    access_token = create_access_token(
        {'sub' : existing_user.email}
    )
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

@router.get("/me")
def get_me(
    current_user = Depends(get_current_user)
    ):
    return current_user
