import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Verify API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ API key missing! Check .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

# Use a stable model (gemini-pro if 1.5 fails)
model = genai.GenerativeModel('gemini-1.5-flash')

# Generate content
try:
    response = model.generate_content("Hello, how are you?")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")