from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

SYSTEM_PROMPT = "You are a helpful study assistant."

def get_response(user_input):
    try:
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_input)
        ]

        response = llm.invoke(messages)
        return response.content

    except Exception as e:
        print("🔥 GROQ ERROR:", repr(e))
        return "Groq API failed"
