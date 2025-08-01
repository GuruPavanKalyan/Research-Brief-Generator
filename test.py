from dotenv import load_dotenv
load_dotenv()

import os
from langsmith import Client

# Make sure keys are loaded
print("API Key:", os.getenv("LANGCHAIN_API_KEY"))

client = Client()

try:
    projects = list(client.list_projects())
    print("Connected to LangSmith. Projects:")
    for p in projects:
        print(f" - {p.name}")
except Exception as e:
    print("LangSmith API failed:", e)

