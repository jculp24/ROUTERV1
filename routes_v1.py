from fastapi import APIRouter
from backend.services.classification_service import classify_query
from backend.services.routing_service import route_model
from backend.api.model_executor import query_openai

router = APIRouter(prefix="/api/v1")

@router.post("/submit-query")
async def submit_query(payload: dict):
    query = payload.get("query")
    task_type = await classify_query(query)
    model = await route_model(task_type)
    response = await query_openai(query, model=model)
    return {"response": response, "model": model}

@router.get("/get-session-history/{user_id}")
async def get_session_history(user_id: str, page: int = 1, limit: int = 20):
    return {"history": [], "page": page, "limit": limit}

@router.post("/feedback")
async def submit_feedback(payload: dict):
    return {"status": "success"}
