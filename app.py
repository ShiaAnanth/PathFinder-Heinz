import streamlit as st
from generate import generate_answer

st.set_page_config(page_title="PathFinder@Heinz", page_icon="🎓")

st.title("PathFinder@Heinz")
st.write("Ask me anything about Heinz College's graduate programs.")

question = st.text_input("Your question:")

if question:
    with st.spinner("Searching handbooks..."):
        answer = generate_answer(question)
    st.write(answer)