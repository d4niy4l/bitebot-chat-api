from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.add_item import router as items_router
from .routes.search import router as search_router

from .pinecone.pinecone_client import get_pinecone_client

@asynccontextmanager
async def init(app: FastAPI):
    get_pinecone_client()
    yield 

app = FastAPI(lifespan=init)



app.include_router(items_router)
app.include_router(search_router)
