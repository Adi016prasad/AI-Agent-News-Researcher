import streamlit as st
from crew import crew
from dotenv import load_dotenv
import os

load_dotenv()

st.title("News Researcher AI Agent")
st.sidebar.title("About the Agents")
st.sidebar.write(
    "This AI Agent uncovers emerging trends and analyzes their potential, providing in-depth insights into opportunities and risks. "
    "It simplifies these findings into compelling, accessible narratives that captivate and educate. "
    "Together, it bridges the gap between discovery and impactful storytelling."
)
topic = st.text_input("News Topic")

if st.button("Run AI Agent"):
    with st.spinner("Processing..."):
        try:
            result = crew.kickoff(inputs={"topic": topic})
            st.success("Task Completed!")
            st.subheader("Result")
            st.text(result)

        except Exception as e:
            st.error(f"An error occurred: {e}")
