from pymongo.errors import DuplicateKeyError
from typing import List
from .classes import CarScraper
from config import settings
from models import Car


async def autoria_filling() -> None:
    scraper = CarScraper(autoria_url=settings.services.autoria)
    cars_data: List[dict] = await scraper.get_full_info()

    cars: List[Car] = [Car(**car_data) for car_data in cars_data]
    for car in cars:
        try:
            await Car.insert(car)
        except DuplicateKeyError:
            continue


async def db_clear() -> None:
    await Car.delete_all()
