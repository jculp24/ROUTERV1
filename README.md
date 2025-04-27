# Dynamic AI Router (MVP)

## Overview
Dynamic routing of queries to the best model (OpenAI, Anthropic, Google, Meta, DeepSeek).

## Backend
- FastAPI server
- Service classes
- API v1 structure
- OpenAPI Docs at `/docs`

## Frontend
- Next.js 14
- TailwindCSS
- ChatGPT-style simple UI

## Installation

```bash
# Backend
cd backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```
