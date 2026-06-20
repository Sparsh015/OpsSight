from datetime import datetime, timedelta
from fastapi import HTTPException, status
from jose import jwt
import os
from models import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.database import get_db


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm= ALGORITHM
    )
    return encoded_jwt

def verify_access_token(token):
    try :
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms= [ALGORITHM])
        email = payload.get("sub")
        return email
    except:
        raise HTTPException(
            status_code= 401,
            detail = "Invalid or expired token"
        )

def get_current_user(
    token = Depends(oauth2_scheme),
    db = Depends(get_db)
    ):

    email = verify_access_token(token)
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )


    return user
