from fastapi import APIRouter
from pydantic import BaseModel
import asyncio

from app.utils.nutrition_api import get_nutrition_data
from app.utils.flatten_item import flatten_item_data
from app.pinecone.insertion import insert_item
from app.llms.llms import mistral
from app.prompts.prompts import insertion_prompt

router = APIRouter(prefix="/items", tags=["items"])

class AddItemBody(BaseModel):
    item_id: int
    name: str
    description: str
    ingredients: list[str]


@router.post("/add")
async def add_item(body:AddItemBody):
    name, description, ingredients = body.name, body.description, body.ingredients
    nutrients = {}
    try:
        ingredient_nutrition_list = await asyncio.gather(*[get_nutrition_data(ingredient) for ingredient in ingredients])

        for ingredient_nutrients in ingredient_nutrition_list:
            for key, value in ingredient_nutrients.items():
                if key in nutrients:
                    nutrients[key]["value"] += value["value"]
                else:
                    nutrients[key] = value

        prompt_text = insertion_prompt.format(name=name, nutrients=nutrients)
        nutrient_description = mistral.invoke(prompt_text)
        print(nutrient_description)
        data = flatten_item_data({
            "item_id": body.item_id,
            "name": name,
            "description": description,
            "ingredients": ingredients,
            "nutrients": nutrients,
            "nutrient_description": nutrient_description.content
        })


        insert_item(data)
        
        response = { 
            "item_id": body.item_id,
            "data": data
        }

        return {"message": "Item has been added", "data": response}
    except Exception as e:
        return {"message": str(e)}, 500
