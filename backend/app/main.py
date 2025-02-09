from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# In-memory database
leaderboard = []

class LeaderboardEntry(BaseModel):
    name: str
    score: int
    timestamp: datetime = datetime.now()

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/api/leaderboard")
async def get_leaderboard() -> List[LeaderboardEntry]:
    try:
        # Return top 5 scores sorted by score in descending order
        sorted_scores = sorted(leaderboard, key=lambda x: x.score, reverse=True)[:5]
        return sorted_scores
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/leaderboard")
async def add_score(entry: LeaderboardEntry):
    try:
        leaderboard.append(entry)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
