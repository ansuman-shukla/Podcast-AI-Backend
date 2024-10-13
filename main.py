from typing import Union
import os
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
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    