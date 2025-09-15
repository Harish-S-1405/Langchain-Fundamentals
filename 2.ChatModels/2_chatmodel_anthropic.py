from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model= 'claude--5-sonnet-20241022')
# we can set temperature and max tokens

result = model.invoke('What is the capital of india')

print(result.content)
