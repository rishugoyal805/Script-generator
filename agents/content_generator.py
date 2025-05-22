import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Setup Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_short_script(theme, context):
    prompt = f"Create a viral 60-second YouTube Shorts script about: {theme}. Trending context: {context}"
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_long_script(theme, context):
    prompt = f"Write a long-form engaging YouTube script (around 5 minutes) for the topic: {theme}. Include data and examples from context: {context}"
    response = model.generate_content(prompt)
    return response.text.strip()
