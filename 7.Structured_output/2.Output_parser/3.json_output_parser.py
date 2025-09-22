from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

# template = PromptTemplate(
#     template='Give me name, age and city of a fictioonal person \n {format_instruction}',
#     input_variables=[],
#     partial_variables={'format_instruction': parser.get_format_instructions()}
# )

# prompt = template.format()

# result = model.invoke(prompt)
# final_result=parser.parse(result.content)

# print(prompt)
# print('=============')
# print(result)
# print('=============')
# print(final_result)
# print('=============')
# print(type(final_result))



template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
