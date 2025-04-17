from pydantic_settings import BaseSettings
import os


class DatabaseSettings(BaseSettings):
    url: str = os.getenv("mongo_url")


class ResponsesSettings(BaseSettings):
    page_size: int = 10


class Config(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()
    response: ResponsesSettings = ResponsesSettings()


settings = Config()
