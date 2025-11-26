import streamlit as st
from gemini_client import get_gemini_response   

# Streamlit page config
st.set_page_config(page_title="Gemini Chatbot")

# Initialize memory in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 Gemini Powered Chatbot")

# Display previous conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Build conversation history to send to Gemini
    full_conversation = "\n".join(
        f"{m['role']}: {m['content']}" for m in st.session_state.messages
    )

    # Get response from Gemini
    bot_reply = get_gemini_response(full_conversation)

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    # Display the latest assistant response
    with st.chat_message("assistant"):
        st.write(bot_reply)
