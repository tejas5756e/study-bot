from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_collection():
    try:
        client = MongoClient(
            os.getenv("MONGO_URI"),
            serverSelectionTimeoutMS=3000
        )
        db = client["study_bot"]
        return db["chat_history"]
    except Exception as e:
        print("MongoDB connection error:", e)
        return None


def save_chat(user_message, bot_response):
    collection = get_collection()
    if collection:
        collection.insert_one({
            "user_message": user_message,
            "bot_response": bot_response
        })


def get_previous_chats(limit=5):
    collection = get_collection()
    if not collection:
        return []
    return list(collection.find().sort("_id", -1).limit(limit))
