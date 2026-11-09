from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(
    uri,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=15000
)

try:
    client.admin.command("ping")
    print("MongoDB Atlas connection successful!")

except Exception as e:
    print("MongoDB connection failed!")
    print(e)

finally:
    client.close()