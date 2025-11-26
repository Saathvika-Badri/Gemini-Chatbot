import streamlit as st
from gemini_client import get_gemini_response

# Streamlit page config
st.set_page_config(page_title="Gemini Chatbot")

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 Gemini Powered Chatbot")

# Display previous conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input box
user_input = st.chat_input("Type your message...")

if user_input:
    # 1️⃣ Immediately display and save user's message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    
    # 2️⃣ Re-render immediately so the message appears without delay
    st.rerun()

# Process the last user message
if st.session_state.messages:
    last_msg = st.session_state.messages[-1]

    # If last message was from the user → generate reply
    if last_msg["role"] == "user":
        full_conversation = "\n".join(
            f"{m['role']}: {m['content']}" for m in st.session_state.messages
        )

        bot_reply = get_gemini_response(full_conversation)

        # Save bot reply
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

        st.rerun()
