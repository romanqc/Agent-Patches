import os
import weaviate
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey

load_dotenv()  # Load variables from .env

weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")

client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=AuthApiKey(weaviate_api_key),
)

# Optional health check
if not client.is_ready():
    raise RuntimeError("Weaviate client is not ready")
