import datetime

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_debug
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
import streamlit as st


set_debug(True)

st.title("Email JSON generator")
product_name = st.text_input("Enter Product Name: ")
features = st.text_input("Enter Feature Name: ")
audience = st.text_input("Enter audience: ")

button = st.button("Run AI")

llm1 = ChatOllama(model="llama3.2:3b")
llm2 = ChatOllama(model="llama3.2-vision:11b")

subject_template = PromptTemplate(
    input_variables=["product", "features"],
    template="""
                You are an intelligent AI assistant who can generate a good email Subject line,
                based on product and its features.
                # Product Name: {product},
                # Product Features: {features}
                Generate a appropriate subject line only within 10 words strictly. 
                No Extra talk.   No Explanation 
            """
)
body_template = PromptTemplate(
    input_variables=["product", "subject", "audience"],
    template="""
                You are an intelligent AI assistant who can generate a good email based on Subject line,
                and product name with target audience.
                # Product Name: {product},
                # Product Email Subject: {subject},
                # Target Audience: {audience}
                Generate the Email body in 150 words.
                No extra talk.  No Explanation.
                
                # Output Must be a JSON only with following keys.
                "product_name", "email_body", "audience", "features", "subject"
                   
            """
)

subject_chain = subject_template | llm1 | StrOutputParser()
email_chain = body_template | llm2 | JsonOutputParser()

final_chaim = subject_chain | (lambda sub: {"subject": sub, "product": product_name, "audience": audience}) | email_chain

if button:
    response = final_chaim.invoke(
        {
            "product": product_name,
            "features": features
        }
    )
    st.write(response)

