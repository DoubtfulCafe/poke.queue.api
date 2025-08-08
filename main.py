import uvicorn
import json
import os
from utils.database import execute_query_json
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
async def root():
    query = "SELECT * FROM pokequeue.MESSAGES"
    result = await execute_query_json(query)
    result_dict = json.loads(result)
    return result_dict

@app.get("/api/version")
async def version():
    return { "version": "0.0.0" }


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)