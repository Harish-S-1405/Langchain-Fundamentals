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

# # pip install -U langchain langchain-huggingface huggingface_hub transformers python-dotenv

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"  # v0.2 is more consistent than v0.1

# llm = HuggingFaceEndpoint(
#     repo_id=MODEL_ID,
#     task="text-generation",
#     max_new_tokens=64,
#     temperature=0.2,    # ok for serverless text-generation
# )

# # 👇 pass tokenizer explicitly so _to_chat_prompt() can apply the chat template
# model = ChatHuggingFace(llm=llm, tokenizer=MODEL_ID)

# result = model.invoke("What is the capital of India?")
# print(result.content)

# from huggingface_hub import InferenceClient

# # Replace with your Hugging Face API token
# HF_TOKEN = "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" 

# client = InferenceClient(token=HF_TOKEN)

# # Choose your desired small model
# model_id = "google/gemma-2-2b-it" 

# prompt = "Write a short story about a cat who discovers a magical garden."
# generated_text = client.text_generation(model=model_id, prompt=prompt, max_new_tokens=100)

# print(generated_text)