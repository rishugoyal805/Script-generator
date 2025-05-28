# main_api.py

from fastapi import FastAPI
from pydantic import BaseModel
from main1 import fetch_features_from_theme, generate_content_from_topic 

app = FastAPI()

class ThemeRequest(BaseModel):
    theme: str

class ContentRequest(BaseModel):
    theme: str
    feature: str
    
@app.get("/")
async def root():
    return {"message": "Welcome to the Theme Feature Generator API!"}

@app.post("/get_features")
async def get_features(req: ThemeRequest):
    sub_topics = await fetch_features_from_theme(req.theme)
    return {"features": sub_topics}

@app.post("/generate_content")
async def generate_content(req: ContentRequest):
    content = await generate_content_from_topic(req.theme, req.feature)
    return {"content": content}
