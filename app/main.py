from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .routes import users
from . import database
app=FastAPI()
app.include_router(users.router)
@app.get("/")
def home(db:Session=Depends(database.get_db)):
  return {"message":"HOME PAGE"}