from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
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
    return FileResponse("ui/index.html")


@app.post("/maintenance")
def maintenance(request: MaintenanceRequest):
    result = maintenance_agent(request.problem)

    return {
        "problem": request.problem,
        "recommendation": result
    }


app.mount("/", StaticFiles(directory="ui", html=True), name="ui") 
