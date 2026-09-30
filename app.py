import streamlit as st
import ollama

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.chat_message("user").write(user_input)

    with st.spinner("Generating response..."):
        response = ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages
        )

        assistant_message = response["message"]["content"]

        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_message
        })

        st.chat_message("assistant").write(assistant_message)