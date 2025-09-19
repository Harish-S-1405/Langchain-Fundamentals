from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 1. Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2. Examples with reasoning (CoT style)
examples = [
    {
        "input": "2 🦜 3",
        "reasoning": "Step 1: 🦜 means addition.\nStep 2: 2 + 3 = 5.",
        "output": "5"
    },
    {
        "input": "2 🐍 4",
        "reasoning": "Step 1: 🐍 means multiplication.\nStep 2: 2 × 4 = 8.",
        "output": "8"
    },
    {
        "input": "If a notebook costs 45 and a pen costs 12, what is total cost of 3 notebooks and 4 pens?",
        "reasoning": "Step 1: Cost of 3 notebooks = 3 × 45 = 135.\nStep 2: Cost of 4 pens = 4 × 12 = 48.\nStep 3: Total cost = 135 + 48 = 183.",
        "output": "183"
    }
]

# 3. Example prompt template (chat style)
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{reasoning}\nFinal Answer: {output}")
])

# 4. Few-shot chat template with examples
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

# 5. Final prompt = system + examples + user input
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful math tutor. Always explain step by step."),
    few_shot_prompt,
    ("human", "{input}")
])

# 6. Format with a user query
user_query = "If a chair costs 150 and a table costs 350, what is total cost of 2 chairs and 1 table?"
formatted_prompt = final_prompt.format_messages(input=user_query)

# print(formatted_prompt)

# print("\n==== Formatted Prompt ====")
# for msg in formatted_prompt:
#     print(f"{msg.type.upper()}: {msg.content}")

# 7. Invoke model
result = model.invoke(formatted_prompt)

print("\n==== Model Output ====")
print(result.content)
