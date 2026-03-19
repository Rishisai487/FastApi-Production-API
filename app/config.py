from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
  DATABASE_USERNAME:str
  DATABASE_PASSWORD:str
  DATABASE_NAME:str
  DATABASE_ADDRESS:str
  SECRET_KEY:str
  ALGORITHM:str
  EXPIRE_MINUTES:int
  model_config=SettingsConfigDict(env_file='.env')

settings=Settings()