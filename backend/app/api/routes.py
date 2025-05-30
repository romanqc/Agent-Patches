from fastapi import APIRouter
from app.services.weaviate_client import client


router = APIRouter()

@router.get("/ask")
def ask_agent(question: str):
    """
    Stub: In the future use LangChain or RAG.
    For now, list schema classes in Weaviate.
    """
    try:
        schema = client.collections.list_all()
        return {"response": f"Schema: {schema}"}
    except Exception as e:
        return {"error": str(e)}

@router.get("/healthz")
async def health_check():
    return {"status": "healthy"}
