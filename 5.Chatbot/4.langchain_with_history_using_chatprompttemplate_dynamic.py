from langchain_core.prompts import ChatPromptTemplate

Chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms , what is {topic}')
])

# Chat_template = ChatPromptTemplate.from_messages([
#     ('system','You are a helpful {domain} expert'),
#     ('human','Explain in simple terms , what is {topic}')
# ])

prompt= Chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)