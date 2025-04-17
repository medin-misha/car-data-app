from models import Car
from schemes.car_schemes import CreateCar, ReturnCar


async def create_car(data: CreateCar) -> ReturnCar:
    return await Car(**data.model_dump()).create()
