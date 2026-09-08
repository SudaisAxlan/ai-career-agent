

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in your .env file")

# Recommended free models right now:

def local_llm():
    llm = ChatGroq( 
    # model="openai/gpt-oss-20b",          # Good & fast (recommended)
    model="openai/gpt-oss-120b",      # Stronger alternative
    # model="qwen/qwen3.6-27b",         # Another good option
    # model="qwen/qwen3.8-27b",
    api_key=api_key,
    temperature=0.7
)
    return llm