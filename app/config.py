from pydantic_settings import BaseSettings
import os


class DatabaseSettings(BaseSettings):
    url: str = os.getenv("mongo_url")

class Config(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()

settings = Config()
