import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL") or "http://localhost:8000/chat"

st.set_page_config(page_title="Coffee Chatbot", page_icon=":coffee:")

st.title("Coffee Chatbot ☕")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input box
user_input = st.text_input("You:", key="user_input")

# When user sends a message
if st.button("Send") and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    try:
        response = requests.post(API_URL, json={"message": user_input})
        if response.status_code == 200:
            bot_reply = response.json().get("response", "(No response from bot)")
        else:
            bot_reply = f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        bot_reply = f"Error: {e}"
    st.session_state.messages.append({"role": "bot", "content": bot_reply})
    # Clear the input by rerunning the app
    st.rerun()

# Display chat history in message containers
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.container():
            st.markdown(
                f"""
                <div style="
                    background-color: #e3f2fd;
                    padding: 10px;
                    border-radius: 10px;
                    margin: 5px 0;
                    text-align: right;
                    color: #000;
                ">
                    <strong>You:</strong><br>
                    {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        with st.container():
            st.markdown(
                f"""
                <div style="
                    background-color: #f5f5f5;
                    padding: 10px;
                    border-radius: 10px;
                    margin: 5px 0;
                    text-align: left;
                    color: #000;
                ">
                    <strong>Bot:</strong><br>
                    {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )