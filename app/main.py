from fastapi import FastAPI
import uvicorn
import asyncio
from db_connect import connect

app = FastAPI()
asyncio.get_event_loop().create_task(connect())



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
