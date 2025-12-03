import streamlit as st

# Import only the objects you created (client, config) WITHOUT running the script
from tool_search import client, config
from google.genai import types

st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")

st.title("💬 Gemini Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


def run_query(query: str) -> str:
    """Call Gemini using your Google Search Tool config."""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
        config=config
    )
    return response.text


# Chat input
user_input = st.chat_input("Ask anything...")

if user_input:
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Respond
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_text = ""

        reply = run_query(user_input)

        # Streaming effect
        for word in reply.split():
            full_text += word + " "
            placeholder.write(full_text)

        # Save reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
