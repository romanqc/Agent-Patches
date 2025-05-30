# backend/app/api/routes.py

from fastapi import APIRouter
from app.services.operant_ai import query_operant_ai

router = APIRouter()

@router.get("/ask")
def ask_agent(question: str):
    """
    Ask the Operant AI agent a question.
    """
    response = query_operant_ai(question)
    return {"response": response}

@router.get("/healthz")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}
