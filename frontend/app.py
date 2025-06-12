# frontend/app.py
import streamlit as st
import requests

st.title("HelpMate Chatbot")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": user_input}
        )
        reply = response.json()["response"]
        st.markdown(f"**HelpMate:** {reply}")
