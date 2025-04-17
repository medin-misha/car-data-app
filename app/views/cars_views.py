from fastapi import APIRouter
from typing import List
from controllers import create_car
from schemes.car_schemes import CreateCar, ReturnCar

router = APIRouter(prefix="/cars", tags=["cars"])


@router.post("/", summary="создание модели Car", response_description="Данные модели Car")
async def create_car_view(car: CreateCar) -> ReturnCar:
    return await create_car(data=car)

