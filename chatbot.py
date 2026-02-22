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

        print("Sending to Groq...")
        response = llm.invoke(messages)

        print("Groq response received")

        answer = response.content
        save_chat(user_input, answer)

        return answer

    except Exception as e:
        print("🔥 CHATBOT ERROR:", repr(e))
        return "LLM error. Check server logs."
