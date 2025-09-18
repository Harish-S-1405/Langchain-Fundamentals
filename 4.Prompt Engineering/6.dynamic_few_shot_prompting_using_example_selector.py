# Example Problem Statement

# 👉 Let’s build a Math Tutor with 🦜 operator again, but now:

# We’ll store multiple examples (🦜 = addition, 🐍 = multiplication).

# Depending on the user’s input, the selector will choose the most relevant examples.

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

# 1. Model
model = ChatOpenAI()

# 2. Examples dataset
examples = [
    {"input": "2 🦜 2", "output": "4"},   # 🦜 means addition
    {"input": "3 🦜 5", "output": "8"},
    {"input": "2 🐍 3", "output": "6"},   # 🐍 means multiplication
    {"input": "4 🐍 5", "output": "20"},
]


# 3. Example Selector using Chroma
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples,
    embeddings=OpenAIEmbeddings(),
    vectorstore_cls=Chroma,
    k=2,  # return top-2 relevant examples
)

# 4. Example prompt template
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Human: {input}\nAI: {output}"
)

# 5. FewShotPromptTemplate with dynamic selector
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="You are a wondrous math wizard.\nHere are some examples:",
    suffix="\nHuman: {user_input}\nAI:",
    input_variables=["user_input"],
)

# 6. User query
user_query = "6 🐍 7"

# ✅ Check which examples were selected
selected = example_selector.select_examples({"input": user_query})
print("==== Selected Examples (Ordered) ====")
for idx, ex in enumerate(selected, 1):
    print(f"Example {idx}:")
    print(f"  input: {ex['input']}")
    print(f"  output: {ex['output']}")

# 7. Format final prompt
final_prompt = dynamic_prompt.format(user_input=user_query)

print("\n==== Final Prompt Sent to Model ====")
print(final_prompt)

# 8. Invoke model
result = model.invoke(final_prompt)
print("\n==== Model Output ====")
print(result.content)