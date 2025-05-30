import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPERANT_API_KEY = os.getenv("OPERANT_API_KEY")
OPERANT_API_URL = os.getenv("OPERANT_API_URL", "https://api.operant.ai/v1/query")

def query_operant_ai(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPERANT_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"input": prompt}

    try:
        response = httpx.post(OPERANT_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("output", "No output returned.")
    except Exception as e:
        return f"Error contacting Operant AI: {e}"
