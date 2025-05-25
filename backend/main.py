import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from models.subscription_model import EmailSubscription
from database import subscriptions

app = FastAPI()

# Fix the static path using absolute location
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../static"))
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

# ✅ Define /subscribe BEFORE mounting /
@app.post("/subscribe")
async def subscribe(data: EmailSubscription):
    subscriptions.insert_one(data.dict())
    return {"status": "ok"}

# ✅ Now mount static + frontend
app.mount("/static", StaticFiles(directory=static_path), name="static")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
