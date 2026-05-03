from fastapi import FastAPI

from app.engine import resolve_mission
from app.models import MissionRequest, MissionResponse

app = FastAPI(
    title="Elyria Mission Control Engine",
    version="0.1.0",
    description="Public proof surface for AI-scientific stage admission.",
)


@app.get("/")
def root():
    return {
        "name": "Elyria Mission Control Engine",
        "proof": "Invalid engineering formation cannot advance stages without safety, standing, monotonicity, receipt, and replay.",
        "public_surface": True,
        "protected_kernel_exposed": False,
    }


@app.post("/mission/resolve", response_model=MissionResponse)
def mission_resolve(req: MissionRequest):
    return resolve_mission(req)


@app.post("/stage/advance", response_model=MissionResponse)
def stage_advance(req: MissionRequest):
    return resolve_mission(req)


@app.post("/claim/attempt", response_model=MissionResponse)
def claim_attempt(req: MissionRequest):
    return resolve_mission(req)


@app.post("/simulation/admit", response_model=MissionResponse)
def simulation_admit(req: MissionRequest):
    return resolve_mission(req)
