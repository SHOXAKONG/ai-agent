import os
import json
from contextlib import asynccontextmanager
from typing import Literal

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPBearer
from pydantic import BaseModel, EmailStr
from decouple import config

from database import init_db
from orchestrator import Orchestrator
from auth import verify_password, create_access_token
from crud import get_user_by_username, get_user_by_email, create_user
from dependencies import get_current_user
from data.mock_data import (
    SALES_DATA, INVENTORY_DATA, FINANCE_DATA, HR_DATA, DASHBOARD_KPIS
)


orchestrator: Orchestrator | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global orchestrator
    init_db()
    api_key = config("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in environment")
    orchestrator = Orchestrator(api_key=api_key)
    yield


app = FastAPI(title="Multi-Agent BI API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Auth schemas ─────────────────────────────────────────────────────────

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: str


# ── Auth routes ──────────────────────────────────────────────────────────

@app.post("/api/auth/register", response_model=UserResponse, status_code=201)
async def register(body: RegisterRequest):
    if get_user_by_username(body.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    if get_user_by_email(body.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if len(body.password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
    user = create_user(body.username, body.email, body.password)
    return user


@app.post("/api/auth/login", response_model=TokenResponse)
async def login(body: LoginRequest):
    user = get_user_by_username(body.username)
    if not user or not verify_password(body.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token = create_access_token({"sub": str(user["id"])})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/api/auth/me", response_model=UserResponse)
async def me(current_user: dict = Depends(get_current_user)):
    return current_user


# ── Chat endpoint (protected) ────────────────────────────────────────────

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    query: str
    history: list[ChatMessage] = []


@app.post("/api/chat")
async def chat(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user),
):
    if orchestrator is None:
        raise HTTPException(status_code=503, detail="Orchestrator not ready")

    history = [m.model_dump() for m in request.history]

    async def event_stream():
        try:
            async for token in orchestrator.stream_response(
                query=request.query,
                history=history,
            ):
                yield f"data: {json.dumps({'token': token})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ── Metrics endpoints (protected) ────────────────────────────────────────

@app.get("/api/metrics/dashboard")
async def get_dashboard(current_user: dict = Depends(get_current_user)):
    return DASHBOARD_KPIS

@app.get("/api/metrics/sales")
async def get_sales(current_user: dict = Depends(get_current_user)):
    return SALES_DATA

@app.get("/api/metrics/inventory")
async def get_inventory(current_user: dict = Depends(get_current_user)):
    return INVENTORY_DATA

@app.get("/api/metrics/finance")
async def get_finance(current_user: dict = Depends(get_current_user)):
    return FINANCE_DATA

@app.get("/api/metrics/hr")
async def get_hr(current_user: dict = Depends(get_current_user)):
    return HR_DATA


# ── Health ───────────────────────────────────────────────────────────────

@app.get("/api/health")
async def health():
    return {"status": "ok"}
