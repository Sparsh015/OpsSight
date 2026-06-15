from datetime import datetime
from pydantic import BaseModel

class UserLogin(BaseModel):
    email : str
    password : str

class UserSignup(BaseModel):
    username : str
    email : str
    password : str 

class UserResponse(BaseModel):
    id : int
    username : str
    email : str
    role : str
    created_at : datetime
