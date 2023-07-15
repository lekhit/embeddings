from sentence_transformers import SentenceTransformer
from fastapi import FastAPI

import json
encoder = SentenceTransformer('all-MiniLM-L6-v2')
print(encoder.encode('hello world'))
app = FastAPI()


@app.get("/")
async def root(query:str='hello world'):
    return {"message": json.dumps(encoder.encode(query).tolist())}
    return {'m':"aasf"}


