from fastapi import APIRouter
from controllers import autoria_filling, db_clear


router = APIRouter(prefix="/db", tags=["database"])


@router.get(
    "/filling", summary="Заполнение базы данных c сайта autoria.", status_code=204
)
async def autoria_filling_database_view() -> None:
    return await autoria_filling()


@router.delete("/", summary="Удалить все записи Car", status_code=204)
async def database_clear_view() -> None:
    return await db_clear()
