from datetime import datetime, timedelta
from fastapi import HTTPException, status
from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
    return email
