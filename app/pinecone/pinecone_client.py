from pinecone import Pinecone
from app.config import PINECONE_API_KEY

pinecone_client = Pinecone(api_key=PINECONE_API_KEY)

if(not pinecone_client.has_index("bitebot")):
    pinecone_client.create_index("bitebot", dimension=384, metric="cosine")

def get_pinecone_client():
    return pinecone_client

