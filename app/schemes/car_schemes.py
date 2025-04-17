from pydantic import BaseModel
from beanie import PydanticObjectId


class BaseCar(BaseModel):
    company: str
    model: str
    production_year: int
    price: float
    mileage: str
    engine: str
    location: str
    photo_url: str


class ReturnCar(BaseCar):
    id: PydanticObjectId


class CreateCar(BaseCar):
    pass
