from passlib.context import CryptContext

pwd_method=CryptContext(schemes=["argon2","bcrypt"],deprecated="auto")

def hash_pwd(raw_password):
  return pwd_method.hash(raw_password)

def verify(raw_password,hashed_password):
  return pwd_method.verify(raw_password,hashed_password)
