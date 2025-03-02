from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.4)

messages = [
    SystemMessage(content='You are a helpful assistant'),
    # HumanMessage(content='Tell me everything about human micro expressions..')
    HumanMessage(content='Tell me capital of India')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)



