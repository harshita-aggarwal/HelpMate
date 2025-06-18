# HelpMate — AI-Powered Context-Aware Support Chatbot

HelpMate is a smart chatbot built with **FastAPI** and **Streamlit**, using **Anthropic Claude** for natural language responses. This project demonstrates how to build an end-to-end AI assistant with modular backend and frontend components.

---

## Features (MVP)
- **FastAPI backend** that processes user messages via an API
- **Streamlit frontend** for an interactive chat interface
- Claude 3 (Anthropic API) for intelligent responses
- Modular project structure for future LLMs, Knowledge base

---

## How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/harshita-aggarwal/helpmate-chatbot.git
cd helpmate-chatbot
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Set Up Claude API Access
This project uses Claude via **Anthropic API**. You'll need:
- An account at https://console.anthropic.com
- Credits in your account (add billing under "Plans & Billing")
- Your API key (format: sk-ant-xxxxxxxxxx)

- Create a .env file in the backend/ folder:
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

**NOTE: DO NOT SHARE THIS KEY PUBLICLY**

### 4. Install Dependencies

- **Backend**
```bash 
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

- **Frontend**
(In a new terminal)
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## Visit and Test
- Backend: http://127.0.0.1:8000
- Frontend: http://localhost:8501
- Type any question - and HelpMate will respond using Claude AI.

## Next Steps
- Integrate OpenAI or Claude for smart responses
- Add knowledge base with LangChain or LlamaIndex
- Add user intent detection
- Dockerize and deploy on AWS

## Author
Harshita Aggarwal