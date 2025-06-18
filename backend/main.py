# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import anthropic

# Loading .env file
load_dotenv()
claude_api_key = os.getenv("ANTHROPIC_API_KEY")

# Seting up Claude client
client = anthropic.Anthropic(api_key=claude_api_key)

app = FastAPI()

# CORS setup to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str
    
    
@app.get("/")
def read_root():
    return {"message": "Welcome to HelpMate backend!"}

@app.post("/chat")
def chat(message: Message):
    user_message = message.message
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",  # You can try Opus or Haiku too
            max_tokens=512,
            temperature=0.7,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.content[0].text
        return {"response": reply}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}
