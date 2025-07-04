from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DB_URL: str = Field(defaut='postgres+asyncpg://admin:admin@localhost/admin')

settings = Settings()