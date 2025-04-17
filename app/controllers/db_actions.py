from fastapi import HTTPException, status
from typing import List
from .classes import CarScraper
from config import settings
from models import Car


async def autoria_filling() -> None:
    try:
        scraper = CarScraper(autoria_url=settings.services.autoria)
        cars_data: List[dict] = await scraper.get_full_info()
        cars: List[Car] = [Car(**car_data) for car_data in cars_data]
        await Car.insert_many(cars)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Извините, но у сервера проблемы с парсингом данных.",
        )


async def db_clear() -> None:
    await Car.delete_all()
