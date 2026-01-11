from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import numpy as np

llm = OllamaEmbeddings(model="nomic-embed-text:latest")

txt1 = input("I1: ")
txt2 = input("I2: ")
res1 = llm.embed_query(txt1)
res2 = llm.embed_query(txt2)

similarity_score = np.dot(res1, res2)

print('Score: ', similarity_score)