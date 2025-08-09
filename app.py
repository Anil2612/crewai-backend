from fastapi import FastAPI
from pydantic import BaseModel
from crew import research_crew

app = FastAPI(title="CrewAI Backend", version="1.0.0")

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "CrewAI Backend is running!"}

@app.post("/run")
def run_task(request: TopicRequest):
    result = research_crew.kickoff({"topic": request.topic})
    return {"topic": request.topic, "results": result}