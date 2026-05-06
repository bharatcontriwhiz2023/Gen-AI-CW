import streamlit as st
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load env
load_dotenv()

# Model
model = ChatMistralAI(model="mistral-medium-3.5", temperature=0.2)

# Page config
st.set_page_config(page_title="CW Chatbot", page_icon="🤖", layout="centered")

# Custom UI Styling
st.markdown(
    """
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
.stChatMessage {
    border-radius: 10px;
    padding: 10px;
}
</style>
""",
    unsafe_allow_html=True,
)

st.title("🤖 CW Chatbot")
st.caption("Choose a mode and start chatting")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False

# Mode selection UI
if not st.session_state.mode_selected:
    st.subheader("🎭 Choose AI Mode")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("😡 Angry"):
            mode = "You are an angry AI agent"
            st.session_state.messages = [SystemMessage(content=mode)]
            st.session_state.mode_selected = True

    with col2:
        if st.button("😂 Funny"):
            mode = "You are a funny AI agent"
            st.session_state.messages = [SystemMessage(content=mode)]
            st.session_state.mode_selected = True

    with col3:
        if st.button("😢 Sad"):
            mode = "You are a sad AI agent"
            st.session_state.messages = [SystemMessage(content=mode)]
            st.session_state.mode_selected = True

    st.stop()

# Chat UI
st.subheader("💬 Chat")

# Display chat history
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
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # Exit condition
    if user_input == "0":
        st.stop()

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.markdown(response.content)
