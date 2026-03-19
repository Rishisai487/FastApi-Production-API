from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from .config import settings

Base=declarative_base()
SQLALCHEMY_URL=f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_ADDRESS}/{settings.DATABASE_NAME}"
engine=create_engine(SQLALCHEMY_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
  db=SessionLocal()
  try:
    yield db
  finally:
    db.close()