from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response

app = FastAPI(title="Study Bot API")

# Request body model
class ChatRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Study Bot is working"}

@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_response(request.query)
    return {"response": reply}