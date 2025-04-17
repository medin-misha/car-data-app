from fastapi import HTTPException, status
from pydantic import ValidationError
from typing import List
from models import Car
from config import settings
from schemes.car_schemes import CreateCar, ReturnCar


async def create_car(data: CreateCar) -> ReturnCar:
    return await Car(**data.model_dump()).create()


async def get_cars(page: int) -> List[ReturnCar]:
    skip_results: int = 0 if 0 <= page <= 1 else page * settings.response.page_size
    return (
        await Car.find().skip(skip_results).limit(settings.response.page_size).to_list()
    )


async def filter_car(filter: dict) -> List[ReturnCar]:
    return await Car.find(filter).to_list()


async def get_car_by_id(id: int) -> ReturnCar:
    try:
        return await Car.get(id)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Машина по id: {id} не найдена",
        )
