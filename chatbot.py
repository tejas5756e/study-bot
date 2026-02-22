from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

from db import save_chat, get_previous_chats

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

SYSTEM_PROMPT = """
You are a Study Bot.
You help students with academic and learning-related questions.
Explain concepts clearly in simple language.
"""

def get_response(user_input):
    try:
        messages = [SystemMessage(content=SYSTEM_PROMPT)]

        previous_chats = get_previous_chats()
        for chat in reversed(previous_chats):
            messages.append(HumanMessage(content=chat["user_message"]))
            messages.append(AIMessage(content=chat["bot_response"]))

        messages.append(HumanMessage(content=user_input))

        # ✅ FIX: use invoke correctly
        response = llm(messages).content

        save_chat(user_input, response)
        return response

    except Exception as e:
        print("ERROR IN CHATBOT:", e)
        return "Sorry, something went wrong on the server."
