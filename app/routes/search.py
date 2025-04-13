from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import re
import json

from app.llms.llms import deepseek, llma_instant, mistral
from app.llms.guardrail import guardrail
from app.utils.classify_query import classify_query
from app.prompts.prompts import complex_query_refinement_prompt, simple_query_refinement_prompt, rerank_query_prompt
from app.pinecone.pinecone_client import get_pinecone_client
from app.embeddings.generate_embeddings import generate_embeddings

router = APIRouter(prefix="/items", tags=["search"])

class SearchBody(BaseModel):
    query: str

def clean_llm_output(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return text.strip()  


@router.post("/search")
async def search(body:SearchBody):
    try:

        query = body.query
        print("User query:", query)
        if not guardrail(query):
            return {"message": "Request rejected due to guardrail breach"}, 403           
        query_type = classify_query(query)
        response = None
        if query_type == "simple":
            prompt = simple_query_refinement_prompt.format(query=query)
            response = llma_instant.invoke(prompt)
        else:
            prompt = complex_query_refinement_prompt.format(query=query)
            response = deepseek.invoke(prompt)
        response = clean_llm_output(response.content)        
        embed_query = generate_embeddings(response)

        pinecone = get_pinecone_client()
        index = pinecone.Index("items")
        index_info = index.describe_index_stats()
        expected_dim = index_info["dimension"]

        if len(embed_query) != expected_dim:
            raise ValueError(f"Embedding dimension mismatch! Expected {expected_dim}, got {len(embed_query)}.")

        search_results = index.query(vector=embed_query, top_k=10, include_metadata=True)
        matches = search_results["matches"]

        print("Matches found:", len(matches))
        results = []

        for match in matches:
            data = {}
            metadata = match["metadata"]
            for key, value in metadata.items():
                if key == "description" or key == "ingredients" or key == "nutrient_description" or key == "name":
                    continue
                if key.endswith("_unit"):
                   continue
                unit_key = f"{key}_unit"
                if unit_key in metadata:
                     data[key] = f"{value} {metadata[unit_key]}"
                else:
                    data[key] = value
            results.append(data)
        reranking_prompt = rerank_query_prompt.format(user_query=query, food_items=results) 

        reranked_response = mistral.invoke(reranking_prompt)
        cleaned = re.sub(r"```json|```", "", reranked_response.content).strip()
        item_id_list = json.loads(cleaned)
        print("Item has been added.")
        print(reranking_prompt)
        print("Reranked response:", item_id_list)
        return {"message": "Search successful", "data": item_id_list}
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)

    
    
