from fastapi import HTTPException, APIRouter
from app.database import SessionLocal
from models import User
from schemas.user import UserSignup, UserResponse
from auth.security import get_password_hash

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
