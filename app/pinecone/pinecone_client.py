from pinecone import Pinecone, ServerlessSpec
from app.config import PINECONE_API_KEY

pinecone_client = None
def get_pinecone_client()->Pinecone:
    global pinecone_client
    if pinecone_client is None:
        pinecone_client = Pinecone(api_key=PINECONE_API_KEY)
        if "items" not in pinecone_client.list_indexes().names():
            pinecone_client.create_index("items", metric="cosine", dimension=1024,  spec=ServerlessSpec(
                                cloud="aws",
                                region="us-east-1"
                            ))
    return pinecone_client

