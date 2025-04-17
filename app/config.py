from pydantic_settings import BaseSettings
import os


class DatabaseSettings(BaseSettings):
    url: str = os.getenv("mongo_url")


class ResponsesSettings(BaseSettings):
    page_size: int = 10

class ServicesUrls(BaseSettings):
    autoria: str = "https://auto.ria.com/car/used/" # я настраивал скрапер только на эту ссылку

class Config(BaseSettings):
    database: DatabaseSettings = DatabaseSettings()
    response: ResponsesSettings = ResponsesSettings()
    services: ServicesUrls = ServicesUrls()


settings = Config()
