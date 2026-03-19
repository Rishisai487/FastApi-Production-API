from fastapi import HTTPException,status,Depends
from jose import jwt,JWTError
from .. import database
from app.models import models
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta,timezone
from ..config import settings
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/users/login")

def create_access_token(payload:dict):
  to_encode=payload.copy()
  to_encode["exp"]=datetime.now(timezone.utc)+timedelta(minutes=settings.EXPIRE_MINUTES)
  jwt_token=jwt.encode(to_encode,key=settings.SECRET_KEY,algorithm=settings.ALGORITHM)
  return jwt_token

def verify_access_token(jwttoken:str):
  try:
    payload=jwt.decode(jwttoken,key=settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    return payload
  except JWTError:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Session Expired")

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
  try:
    payload=verify_access_token(token)
    user=db.query(models.User).filter(models.User.id==payload["id"]).first()
    return user
  except JWTError:
    raise HTTPException(status_code=401,detail="Not Authorized")
