from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGO_URI or not DATABASE_NAME:
    raise ValueError("Missing required environment variables: MONGO_URI or DATABASE_NAME")

client = AsyncIOMotorClient(MONGO_URI)
engine = AIOEngine(client=client, database=DATABASE_NAME)