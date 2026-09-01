from fastapi import FastAPI
from pydantic import BaseModel

from app.agent.agent import maintenance_agent


app = FastAPI(
    title="Prescriptive Maintenance RAG Agent",
    description="RAG-based maintenance recommendation API",
    version="1.0.0"
)


class MaintenanceRequest(BaseModel):
    problem: str


@app.get("/")
def root():
    return {
        "message": "Prescriptive Maintenance RAG Agent API is running"
    }


@app.post("/maintenance")
def maintenance(request: MaintenanceRequest):
    result = maintenance_agent(request.problem)

    return {
        "problem": request.problem,
        "recommendation": result
    }
