from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from dotenv import load_dotenv


load_dotenv()

# 1. Model
model = ChatOpenAI()

# 1. Examples
examples = [
    {"input": "2 🦜 2", "output": "4"},
    {"input": "2 🦜 3", "output": "5"},
    {"input": "2 🦜 4", "output": "6"},
    {"input": "What did the cow say to the moon?", "output": "nothing at all"},
    {
        "input": "Write me a poem about the moon",
        "output": "One for the moon, and one for me, who are we to talk about the moon?",
    },
]

# 2. Build vectorstore
to_vectorize = [" ".join(example.values()) for example in examples]
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=examples)

# 3. Example selector
example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2)

# 4. Example prompt template
example_prompt = ChatPromptTemplate.from_messages(
        [("human", "{input}"), ("ai", "{output}")]
)

# 4. Few-shot prompt
few_shot_prompt = FewShotChatMessagePromptTemplate(
    # input_variables=["input"],
    example_selector=example_selector,
    example_prompt= example_prompt
    )


# print(few_shot_prompt.invoke(input="What's 3 🦜 3?").to_messages())


# 5. Final prompt with system role + examples + user input
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a wondrous wizard of math."),
    few_shot_prompt,
    ("human", "{input}"),
])

# print(final_prompt.invoke(input="What's 3 🦜 3?"))

user_query = "write a poem on earth"
# 6. Inspect how the examples are injected
formatted_prompt = final_prompt.format_messages(input=user_query)
print(formatted_prompt)
# print("==== Formatted Prompt Messages ====")
# for msg in formatted_prompt:
#     print(f"{msg.type.upper()}: {msg.content}")

result = model.invoke(formatted_prompt)
print("\n==== Model Output ====")
print(result.content)
