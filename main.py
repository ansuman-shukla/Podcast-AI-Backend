from typing import Union

from fastapi import FastAPI
from services.querry import query
from services.embedder import embedder
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ask")
async def read_item(userQuery: str):
    response = query(userQuery)
    return response

@app.get("/post")
def postLink(youtubeLink: str):
    embedder(youtubeLink)
    return {"status": "success"}
    
