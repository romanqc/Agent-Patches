import os
from weaviate import Client
from weaviate.auth import AuthApiKey

def get_client():
    auth = AuthApiKey(api_key=os.environ["WEAVIATE_API_KEY"])
    return Client(url=os.environ["WEAVIATE_URL"], auth_client_secret=auth)
