from fastapi import APIRouter, Depends
from app.services.weaviate_client import get_client

router = APIRouter()

@router.get("/ask")
def ask_agent(question: str, client = Depends(get_client)):
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
    return {"status": "ok"}  # ✅ Match test expectation

