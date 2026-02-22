from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))

# Create / use database
db = client["study_bot"]

# Create / use collection
collection = db["chat_history"]

def save_chat(user_message, bot_response):
    collection.insert_one({
        "user_message": user_message,
        "bot_response": bot_response
    })

def get_previous_chats(limit=5):
    chats = collection.find({}, {"_id": 0}).sort("_id", -1).limit(limit)
    return list(chats)
