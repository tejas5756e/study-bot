# Study Bot – AI Chatbot Project

## Project Description
Study Bot is an AI-powered chatbot that helps students by answering academic and study-related questions.  
It uses a Large Language Model (LLM) and stores previous conversations in MongoDB to provide context-aware responses.

## Technologies Used
- Python
- FastAPI
- LangChain
- Groq LLM (LLaMA 3.1)
- MongoDB Atlas
- Uvicorn

## Features
- Ask study-related questions
- Context-aware responses using MongoDB chat history
- REST API with Swagger UI

## API Endpoints
- `GET /` – Health check
- `POST /chat` – Ask questions to the Study Bot

## How to Run Locally
```bash
pip install -r requirements.txt
uvicorn app:app

Open:

http://127.0.0.1:8000/docs


Click post 

Enter Question in Query in proper format



Author
Tejas Mago