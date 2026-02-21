from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
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
Use previous conversation context to give better answers.
Explain concepts clearly in simple language.
"""

def get_response(user_input):
    messages = []

    # System prompt
    messages.append(("system", SYSTEM_PROMPT))

    # Previous chat memory
    previous_chats = get_previous_chats()
    for chat in reversed(previous_chats):
        messages.append(("human", chat["user_message"]))
        messages.append(("ai", chat["bot_response"]))

    # Current user input
    messages.append(("human", user_input))

    # Convert to prompt
    prompt = ChatPromptTemplate.from_messages(messages)

    # Invoke model correctly
    response = llm.invoke(prompt.format_messages()).content

    # Save to DB
    save_chat(user_input, response)

    return response