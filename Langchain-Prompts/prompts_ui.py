from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Research Tool')

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature = 0.4)
user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)