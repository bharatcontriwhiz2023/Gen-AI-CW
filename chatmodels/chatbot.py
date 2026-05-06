from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatMistralAI(model="mistral-medium-3.5", temperature=0.2)
print("Choose your AI mode")
print("1 for angry mode")
print("2 for funny mode")
print("3 for sad mode")
choice = int(input("please choose your mode to get response:"))
if choice == 1:
    mode = "You are an angry AI agent"
elif choice == 2:
    mode = "You are a funny AI agent"
elif choice == 3:
    mode = "You are a sad AI agent"

# messages = [SystemMessage(content="You are an AI teacher")]
messages = [SystemMessage(content=mode)]
print("Welcome to CW chatbot")
while True:
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot :", response.content)

print(messages)
