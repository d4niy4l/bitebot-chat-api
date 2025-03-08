from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")
NUTRITION_API_URL = os.getenv("NUTRITION_API_URL")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")