# HelpMate — AI-Powered Context-Aware Support Chatbot

HelpMate is a smart support chatbot that combines natural language understanding with a clean user interface. Built with **FastAPI** on the backend and **Streamlit** on the frontend, it's designed to be simple, powerful, and easily extendable with LLMs like OpenAI or Claude.

---

## Features (MVP)
- **FastAPI backend** that processes user messages via an API
- **Streamlit frontend** for an interactive chat interface
- Seamless communication between UI and backend
- Ready for LLM integration (OpenAI, Claude)
- Clean project structure with virtual environment support

---

## How to Run Locally

### 1. Clone the repo
git clone https://github.com/harshita-aggarwal/helpmate-chatbot.git
cd helpmate-chatbot

### 2. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

- **Backend**
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

- **Frontend**
(In a new terminal)
cd frontend
pip install -r requirements.txt
streamlit run app.py

## Visit and Test
- Backend: http://127.0.0.1:8000
- Frontend: http://localhost:8501

## Next Steps
- Integrate OpenAI or Claude for smart responses
- Add knowledge base with LangChain or LlamaIndex
- Add user intent detection
- Dockerize and deploy on AWS

## Author
Harshita Aggarwal