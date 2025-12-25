import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.globals import set_debug

set_debug(True)

st.title('Ask AI Anything')
prompt = st.text_input("Enter a question: ")

llm = ChatOllama(model="llama3.2-vision:11b")

if prompt:
    res = llm.invoke(prompt)
    st.write(res.content)
