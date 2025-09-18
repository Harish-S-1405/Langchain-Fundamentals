from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 1. Model
model = ChatOpenAI()

# 2. Examples dataset (static list)
examples = [
    {"input": "2 🦜 2", "output": "4"},
    {"input": "3 🦜 5", "output": "8"},
    {"input": "2 🐍 3", "output": "6"},
    {"input": "4 🐍 5", "output": "20"},
]

# 3. Example chat template (how each example looks)
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

# 4. Few-shot chat template (no selector → just static examples)
few_shot_chat_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples
)

print(few_shot_chat_prompt.invoke({}).to_messages())

# 5. Final chat prompt template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a wondrous math wizard."),
    few_shot_chat_prompt,
    ("human", "{input}")
])

# 6. Format the prompt
user_query = "6 🐍 7"
formatted_prompt = chat_prompt.format_messages(input=user_query)

# print("==== Formatted Prompt Messages ====")
# for msg in formatted_prompt:
#     print(f"{msg.type.upper()}: {msg.content}")

# 7. Invoke model
result = model.invoke(formatted_prompt)
print("\n==== Model Output ====")
print(result.content)
