import os
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama


openai_key = os.getenv("OPEN_API_KEY")

# print(openai_key)
# llm = ChatOpenAI(model="gpt-4o", api_key=openai_key)
llm = ChatOllama(model="llama3.2-vision:11b")

prompt = input("Enter a question to AI: ")

res = llm.invoke(prompt)
print(type(res))
print(res.content)