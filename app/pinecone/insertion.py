from app.pinecone.pinecone_client import get_pinecone_client
from app.embeddings.generate_embeddings import generate_embeddings

def insert_item(food_data):
    pinecone = get_pinecone_client()
    embeddings = generate_embeddings(f"{food_data['name']} {food_data['description']} {food_data['ingredients']} {food_data['nutrient_description']}")
    index = pinecone.Index("items")
    index.upsert(
        vectors=[(str(food_data["item_id"]), embeddings, food_data)],
    )