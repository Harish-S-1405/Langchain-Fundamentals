from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

load_dotenv()

model = ChatOpenAI()

# result=model.invoke("What is 2 🦜 9?")

# output =I'm sorry, but I cannot provide an answer to this question as it does not make mathematical sense. Please provide a valid mathematical expression for me to help you with.
# print(result.content)

examples = [
    {"input": "2 🦜 2", "output": "4"},
    {"input": "2 🦜 3", "output": "5"},
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt   
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a wondrous wizard of math."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

formatted_prompt = final_prompt.format_messages(input="2 🦜 9")

result = model.invoke(formatted_prompt)

print(result.content)