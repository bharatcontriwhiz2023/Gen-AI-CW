from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-medium-3.5")
response = model.invoke("What is HTML")
print(response.content)
