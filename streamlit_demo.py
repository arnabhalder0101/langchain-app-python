import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.globals import set_debug
# from langchain_groq import ChatGroq


set_debug(True)

# api_key = os.getenv("GROQ_API_KEY")

st.title('Ask AI Anything')
prompt = st.text_input("Enter a question: ")

llm = ChatOllama(model="llama3.2-vision:11b")
# llm = ChatOllama(model="allam-2-7b")

if prompt:
    res = llm.invoke(prompt)
    st.write(res.content)
