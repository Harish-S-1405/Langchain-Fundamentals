from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Fetch key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Pass the key to the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Ask a question
result = model.invoke("What is the capital of India?")

print(result.content)




