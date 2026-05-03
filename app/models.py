from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class Stage(str, Enum):
    DESIGN_NOTE = "DESIGN_NOTE"
    SIMULATION_REQUEST = "SIMULATION_REQUEST"
    CONTROLLED_REVIEW = "CONTROLLED_REVIEW"
    CERTIFICATION_PACKET = "CERTIFICATION_PACKET"


class MissionOutcome(str, Enum):
    ADMIT = "ADMIT"
    HOLD = "HOLD"
    REBOUND = "REBOUND"
    REFUSE = "REFUSE"
    HALT = "HALT"
    QUARANTINE = "QUARANTINE"
    CERTIFY = "CERTIFY"


class MissionRequest(BaseModel):
    candidate_id: str
    corridor_id: str = "aerospace_surrogate_corridor_v0_1"
    stage_from: Stage = Stage.DESIGN_NOTE
    stage_to: Stage = Stage.SIMULATION_REQUEST
    safety_passed: bool = True
    evidence_complete: bool = True
    witness_present: bool = True
    monotone_stage_move: bool = True
    contamination_signal: float = Field(default=0.0, ge=0.0)
    integrity_ok: bool = True
    certification_requested: bool = False
    public_summary: str = "surrogate engineering formation"


class MissionResponse(BaseModel):
    outcome: MissionOutcome
    advanced: bool
    invariant_holds: bool
    reason_code: str
    mission_decision_id: str
    receipt_hash: str
    replay_token: str
    receipt: dict[str, Any]
