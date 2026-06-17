import streamlit as st

st.set_page_config(page_title="AI Financial Assistant")

st.title("🏦 AI Financial Assistant")

question = st.text_input("Ask a banking question")

if question:
    st.success(f"You asked: {question}")