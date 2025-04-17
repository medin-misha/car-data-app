from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from config import settings
from models import Car

async def connect():
    client: AsyncIOMotorClient = AsyncIOMotorClient(settings.database.url)
    await init_beanie(database=client["cars"], document_models=[Car])
