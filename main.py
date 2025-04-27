from fastapi import FastAPI
from backend.api.routes_v1 import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Dynamic AI Model Router",
    description="MVP API for classifying, routing, and responding to user queries.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
