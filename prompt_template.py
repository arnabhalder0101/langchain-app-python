import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.globals import set_debug
from langchain_core.prompts import PromptTemplate

set_debug(True)

st.title('Ask AI About Cuisine of countries')
country = st.text_input("Enter a country name: ")
no_of_sentence = st.number_input("Enter how many Paras: ", max_value=5, min_value=1)
language = st.text_input("Enter a language: ")

button = st.button("Run")

llm = ChatOllama(model="llama3.2-vision:11b")

prompt_template = PromptTemplate(
    input_variables=["country", "no_of_sentence", "lang"],
    template=""""You are a expert in traditional cuisines. You provide information about 
             specific dish from specific country.
             ## Rules:
             
             - Avoid answering stupid things. if country is imaginary or misleading just reply "I Don't Know!".
             - User can use short forms of country. distinguish it carefully.
             - Human can do spelling mistake. If you think its unintentional spell mistake then try to answer with your guessed
               country.
             
             Answer the question in {no_of_sentence} short paras: What is the traditional cuisine of country: {country}?
             Answer in {lang} language only"""

)

if button:
    res = llm.invoke(prompt_template.format(country=country, no_of_sentence=no_of_sentence, lang=language))
    st.write(res.content)
