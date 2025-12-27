import datetime

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_debug
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
import streamlit as st

set_debug(True)

st.title('Ask AI to generate a speech for a topic')
topic = st.text_input("Enter a Topic: ")
emotion = st.text_input("Enter an Emotion: ")

button = st.button("Run")

llm1 = ChatOllama(model="llama3.2:3b")
llm2 = ChatOllama(model="llama3.2-vision:11b")

title_template = PromptTemplate(
    input_variables=["topic"],
    template="""
            You are the best speech writer in the world.
            You have to create a creative title for the speech on the topic: {topic} .
            
            ## Rules: 
            - Answer in exactly one title. 
            - Do Not Explain.
            
            """
)

speech_template = PromptTemplate(
    input_variables=["title", "user_input", "emotion"],
    template="""
            You are the best speech writer in the world.
            You have to write a creative and {emotion} speech for the title: {title}.
            the user input topic is: {user_input}. Use it for better relevance. 
            ## Rules: 
            - Answer in 300 words.
            - Do Not Explain.
            - Always keep the title on top. Then write the speech.
            - Output must be a JSON format with following keys:
              "user_input", "title", "speech" 
            
            """
)

first_chain = title_template | llm1 | StrOutputParser()  # | (lambda title: (st.write(title), title)[1])
second_chain = speech_template | llm2 | JsonOutputParser()
final_chain = first_chain | (lambda title: {"title": title, "user_input": topic, "emotion": emotion}) | second_chain

if button:
    time1 = datetime.datetime.now().
    res = final_chain.invoke(
        {"topic": topic}
    )
    time2 = datetime.datetime.now()

    st.write("Time Taken: ", time2-time1)
    st.write(res)
