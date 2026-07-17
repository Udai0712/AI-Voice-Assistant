import os
from dotenv import load_dotenv
from google import genai

print("Starting...")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded:", api_key is not None)

client = genai.Client(api_key=api_key)

print("Fetching models...")

try:
    models = client.models.list()

    found = False
    for model in models:
        found = True
        print(model.name)

    if not found:
        print("No models returned.")

except Exception as e:
    print("Error:", e)