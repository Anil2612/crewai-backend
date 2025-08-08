import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from services.crew_service import run_research_and_writing

app = FastAPI(title="CrewAI Backend", version="1.0.0")

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "CrewAI Backend is running!"}

print("Token:", os.getenv("HUGGINGFACE_API_TOKEN"))  # Should print your token

@app.post("/run")
def run_task(request: TopicRequest):
    results = run_research_and_writing(request.topic)
    return {"topic": request.topic, "results": results}

print('__name__', __name__)
if __name__ == "__main__":
    port = 8002
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
