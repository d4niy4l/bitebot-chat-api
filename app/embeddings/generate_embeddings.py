from langchain_mistralai import MistralAIEmbeddings

from app.config import MISTRAL_API_KEY

mistralai_embeddings = MistralAIEmbeddings(api_key=MISTRAL_API_KEY)

def generate_embeddings(text:str)->list:
    return mistralai_embeddings.embed_query(text)