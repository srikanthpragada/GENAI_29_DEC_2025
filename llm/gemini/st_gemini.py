import streamlit as st
from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

st.title("LLM Demo")
prompt = st.text_input("Enter your Prompt", "")

if len(prompt) > 0:
    response = model.invoke(prompt)
    st.write(f"{response.content}")
     
