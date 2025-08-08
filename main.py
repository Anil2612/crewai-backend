from fastapi import FastAPI
from pydantic import BaseModel
from services.crew_service import run_research_and_writing

app = FastAPI(title="CrewAI Backend", version="1.0.0")

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "CrewAI Backend is running!"}

@app.post("/run")
def run_task(request: TopicRequest):
    results = run_research_and_writing(request.topic)
    return {"topic": request.topic, "results": results}
