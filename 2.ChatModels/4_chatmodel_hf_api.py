from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3"   # or "meta-llama/Llama-3.1-8B-Instruct" ,meta-llama/Llama-3.2-1B-Instruct , meta-llama/Llama-3.2-3B-Instruct ,google/flan-t5-small
    # task="text-generation"
)

# print(llm)

model = ChatHuggingFace(llm=llm)


result = model.invoke("What is the capital of India")

print(result.content)

