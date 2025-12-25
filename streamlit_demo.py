import streamlit as st

# from langchain_ollama import ChatOllama
from langchain_core.globals import set_debug
from langchain_groq import ChatGroq


set_debug(True)

st.title('Ask AI Anything')
prompt = st.text_input("Enter a question: ")

# llm = ChatOllama(model="llama3.2-vision:11b")
llm = ChatGroq(model="llama3.2-vision:11b", api_key="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")

if prompt:
    res = llm.invoke(prompt)
    st.write(res.content)
