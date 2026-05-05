from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatMistralAI(model="mistral-medium-3.5", temperature=0.2, max_tokens=10)

response = model.invoke("write a joke on ironman")

print(response.content)
