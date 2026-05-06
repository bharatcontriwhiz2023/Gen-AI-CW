import streamlit as st
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load env variables
load_dotenv()

# Initialize model
model = ChatMistralAI(model="mistral-medium-3.5", temperature=0.2)

# Streamlit page config
st.set_page_config(page_title="CW Chatbot", page_icon="🤖")
st.title("🤖 CW Chatbot")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="You are an AI teacher")]

# Display chat history (skip system message in UI)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # Exit condition
    if user_input == "0":
        st.stop()

    # Get response from model
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.markdown(response.content)
