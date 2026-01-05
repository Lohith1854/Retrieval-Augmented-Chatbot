import streamlit as st
from rag_engine import generate_answer

st.set_page_config(page_title="Gemini RAG Chatbot", layout="centered")

st.title("💬 Gemini RAG Chatbot")
st.write("Ask questions based on company documents")

question = st.text_input("Enter your question")

if question:
    with st.spinner("Thinking..."):
        answer = generate_answer(question)
    st.success("Answer:")
    st.write(answer)
