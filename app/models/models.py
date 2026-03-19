from sqlalchemy import Integer,String,DateTime,Boolean,Column 
from ..database import Base

class User(Base):
  __tablename__="user"
  id=Column(Integer,nullable=False,primary_key=True)
  username=Column(String,nullable=False,unique=True)
  email=Column(String,nullable=False,unique=True)
  password=Column(String,nullable=False)
  Role=Column(String,nullable=False,server_default="user")
