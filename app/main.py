from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from db_connect import connect
from views import cars_router, db_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    await connect()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(cars_router)
app.include_router(db_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
