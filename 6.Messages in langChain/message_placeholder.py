from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

query = "Where is my refund"

# append the user's message to chat history
chat_history.append(HumanMessage(content=query))

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':query})

result = model.invoke(prompt)
chat_history.append(AIMessage(content=result.content))

print("AI: ",result.content)

print(chat_history)
