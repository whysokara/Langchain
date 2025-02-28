from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature = 0.4)
result = model.invoke("What is capital of India?")

print(result.content)