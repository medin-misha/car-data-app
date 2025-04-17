from fastapi import APIRouter
from typing import List
from controllers import create_car, get_cars
from schemes.car_schemes import CreateCar, ReturnCar

router = APIRouter(prefix="/cars", tags=["cars"])


@router.post(
    "/", summary="Создание модели Car", response_description="Данные модели Car"
)
async def create_car_view(car: CreateCar) -> ReturnCar:
    return await create_car(data=car)


@router.get(
    "/",
    summary="Получение данных Car постранично",
    response_description="Страница записей модели Car",
)
async def get_cars_view(page: int = 1) -> List[ReturnCar]:
    return await get_cars(page=page)
