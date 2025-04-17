from fastapi import APIRouter, status, HTTPException
from typing import List
from controllers import (
    create_car,
    get_cars,
    filter_car,
    get_car_by_id,
    delete_car_by_id,
    update_car_by_id,
)
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


@router.get(
    "/make/{company}",
    summary="Получение списка Car по компании производителя",
    response_description="Список Car",
)
async def get_car_by_company_view(company: str) -> List[ReturnCar]:
    return await filter_car(filter={"company": company})


@router.get(
    "/year/{year}",
    summary="Получение списка Car по году выпуска",
    response_description="Список Car",
)
async def get_car_by_production_year_view(year: int) -> List[ReturnCar]:
    return await filter_car(filter={"production_year": year})


@router.get(
    "/{id}", summary="Получение Car по его id", response_description="Данные модели Car"
)
async def get_car_by_id_view(id: str) -> ReturnCar | None:
    return await get_car_by_id(id=id)


@router.put(
    "/{id}", summary="Обновлениме car по его id", response_description="Обновлённый Car"
)
async def update_car_by_id_view(id: str, car_data: CreateCar):
    return await update_car_by_id(id=id, data=car_data)


@router.delete("/{id}", summary="Удаление Car по его id", status_code=204)
async def delete_car_by_id_view(id: str) -> None:
    return await delete_car_by_id(id=id)
