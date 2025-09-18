from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize model
model = ChatOpenAI()

# 2. Start conversation history
chat_history = [
    SystemMessage(content="You are a helpful math assistant."),
    HumanMessage(content="In our math world, 🦜 means addition."),
    AIMessage(content="Understood! I will treat 🦜 as addition."),
]

# 3. Add a new user query
chat_history.append(HumanMessage(content="What is 2 🦜 9?"))

# 4. Invoke model with full history
result = model.invoke(chat_history)

# 5. Print response
print(result.content)ss
