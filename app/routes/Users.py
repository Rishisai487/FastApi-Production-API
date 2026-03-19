from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from .. import database
from .. import utils
from ..schemas import Schemas
from ..models import models
from app.routes import oauth2
router=APIRouter(prefix="/users",tags=["USERS"])

@router.post("/create")
def create(data:Schemas.User,db:Session=Depends(database.get_db)):
  data.password=utils.hash_pwd(data.password)
  user=models.User(**data.model_dump())
  try:
    db.add(user)
    db.commit()
  except:
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="Username or email already exists!")
  return {"message":"User Created Succesfully!"}

@router.post("/login")
def login(credentials:Schemas.User_Login,db:Session=Depends(database.get_db)):
  user=db.query(models.User).filter(models.User.email==credentials.email).first()
  if not user:
    raise HTTPException(status_code=404,detail="User not Found")
  if utils.verify(credentials.password,user.password):
    jwt_token=oauth2.create_access_token({"id":user.id})
    return {"access_token":jwt_token,"token_type":"bearer_token"}     
  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Email or Password")

@router.get("/data")
def data(user=Depends(oauth2.get_current_user)):
  return {"message":"Its working"}