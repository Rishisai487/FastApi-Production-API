from pydantic import BaseModel

class User(BaseModel):
  username:str
  email:str
  password:str

class User_Login(BaseModel):
  email:str
  password:str