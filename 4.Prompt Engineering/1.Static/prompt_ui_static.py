from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI()

st.header('Research Tool')

user_input=st.text_input('Enter your Prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)

# you are giving complete control to user , LLM is prompt sesitive
# to have consistent user experience , if we are asking prompt from user then this goal wont be achieved