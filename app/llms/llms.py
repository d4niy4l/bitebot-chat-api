from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

deepseek = ChatGroq(
    temperature=0.5,
    model="deepseek-r1-distill-qwen-32b",
    api_key=GROQ_API_KEY
)

llma_instant = ChatGroq(
    temperature=0.5,
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY
)

mistral = ChatGroq(
    temperature=0.5,
    model="mistral-saba-24b",
    api_key=GROQ_API_KEY
)

gemma = ChatGroq(   
    temperature=0,
    model="gemma2-9b-it",
    api_key=GROQ_API_KEY
)