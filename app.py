import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
print("KEY =", os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Financial Assistant")

st.title("🏦 AI Financial Assistant")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

question = st.text_input("Ask a banking question")

if question:
    response = llm.invoke(question)
    st.write(response.content)