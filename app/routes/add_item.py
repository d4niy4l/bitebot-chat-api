from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/items", tags=["items"])

class AddItemBody(BaseModel):
    name: str
    description: str
    ingredients: list[str]


@router.post("/add")
async def add_item(body:AddItemBody):
    
    return {"message": "Item has been created"}

