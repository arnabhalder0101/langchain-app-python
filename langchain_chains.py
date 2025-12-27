from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_debug
import streamlit as st

set_debug(True)

st.title('Ask AI About Cuisine of countries')
city = st.text_input("Enter a city name: ")
month = st.text_input("Enter month name: ")
budget = st.selectbox("Travel budget", ["Low", "Medium", "High"])
language = st.text_input("Enter language: ")

button = st.button("Run")

llm = ChatOllama(model="llama3.2-vision:11b")




template = PromptTemplate(
    input_variables=["city","month", "language", "budget"],
    template="""
            You are the best Travel guide of any city or town in the world.
            You need to guide for travel in {city} city/town visiting in {month} month.
            Provide Guide:
            1. Must Visit Places.
            2. Cuisine to try.
            3. Useful phrases in {language}.
            4. Tips for travel in {budget} budget.
         
            
            """
)



if button:
    res = llm.invoke(template.format(
        city=city,
        budget=budget,
        language=language,
        month=month
    ))
    st.write(res.content)



