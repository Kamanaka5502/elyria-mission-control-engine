import hashlib
import json
from typing import Any

POLICY = {
    "policy_id": "ELYRIA_MISSION_CONTROL_INVARIANT_v0_1",
    "invariant": "NO_UNSAFE_UNWITNESSED_NONMONOTONE_OR_INVALID_FORMATION_MAY_ADVANCE",
    "public_surface": True,
    "protected_kernel_exposed": False,
}


def canonical(obj: Any) -> str:
    if hasattr(obj, "model_dump"):
        obj = obj.model_dump(mode="json")
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def sha256(obj: Any) -> str:
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()


def make_receipt(request, outcome: str, advanced: bool, reason_code: str, invariant_holds: bool) -> dict:
    candidate_hash = sha256({
        "candidate_id": request.candidate_id,
        "public_summary": request.public_summary,
    })
    policy_hash = sha256(POLICY)
    witness_hash = sha256({
        "witness_present": request.witness_present,
        "corridor_id": request.corridor_id,
    })
    core = {
        "corridor_id": request.corridor_id,
        "stage_from": request.stage_from.value,
        "stage_to": request.stage_to.value,
        "candidate_hash": candidate_hash,
        "policy_hash": policy_hash,
        "witness_hash": witness_hash,
        "outcome": outcome,
        "reason_code": reason_code,
        "advanced": advanced,
        "invariant_holds": invariant_holds,
    }
    mission_decision_id = "md_" + sha256(core)[:16]
    receipt_hash = sha256({"mission_decision_id": mission_decision_id, "core": core})
    replay_token = "replay_" + sha256({"receipt_hash": receipt_hash, "core": core})[:24]
    return {
        "mission_decision_id": mission_decision_id,
        **core,
        "receipt_hash": receipt_hash,
        "replay_token": replay_token,
    }
