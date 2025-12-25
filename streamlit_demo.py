import streamlit as st

from langchain_ollama import ChatOllama

st.title('Ask AI Anything')
prompt = st.text_input("Enter a question: ")

llm = ChatOllama(model="llama3.2-vision:11b")

if prompt:
    res = llm.invoke(prompt)
    st.write(res.content)
