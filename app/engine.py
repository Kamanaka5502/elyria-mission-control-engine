from app.models import MissionOutcome, MissionRequest, MissionResponse, Stage
from app.receipts import make_receipt

ORDER = [
    Stage.DESIGN_NOTE,
    Stage.SIMULATION_REQUEST,
    Stage.CONTROLLED_REVIEW,
    Stage.CERTIFICATION_PACKET,
]


def is_monotone_stage_move(stage_from: Stage, stage_to: Stage) -> bool:
    try:
        return ORDER.index(stage_to) == ORDER.index(stage_from) + 1
    except ValueError:
        return False


def resolve_mission(req: MissionRequest) -> MissionResponse:
    structural_monotone = is_monotone_stage_move(req.stage_from, req.stage_to)
    monotone_ok = req.monotone_stage_move and structural_monotone

    if not req.integrity_ok:
        outcome = MissionOutcome.HALT
        reason_code = "INTEGRITY_FAILURE"
    elif req.contamination_signal >= 2.0:
        outcome = MissionOutcome.QUARANTINE
        reason_code = "FORMATION_CONTAMINATED"
    elif not req.safety_passed:
        outcome = MissionOutcome.HALT
        reason_code = "SAFETY_GATE_FAILED"
    elif not req.evidence_complete:
        outcome = MissionOutcome.HOLD
        reason_code = "EVIDENCE_INCOMPLETE"
    elif not req.witness_present:
        outcome = MissionOutcome.REFUSE
        reason_code = "WITNESS_ABSENT"
    elif not monotone_ok:
        outcome = MissionOutcome.REBOUND
        reason_code = "NON_MONOTONE_STAGE_MOVE"
    elif req.certification_requested and req.stage_to == Stage.CERTIFICATION_PACKET:
        outcome = MissionOutcome.CERTIFY
        reason_code = "BOUNDED_CERTIFICATION_PACKET_READY"
    else:
        outcome = MissionOutcome.ADMIT
        reason_code = "STAGE_ADVANCEMENT_ADMITTED"

    advanced = outcome in {MissionOutcome.ADMIT, MissionOutcome.CERTIFY}
    invariant_holds = advanced == (
        req.safety_passed
        and req.evidence_complete
        and req.witness_present
        and monotone_ok
        and req.integrity_ok
        and req.contamination_signal < 2.0
    )

    receipt = make_receipt(req, outcome.value, advanced, reason_code, invariant_holds)

    return MissionResponse(
        outcome=outcome,
        advanced=advanced,
        invariant_holds=invariant_holds,
        reason_code=reason_code,
        mission_decision_id=receipt["mission_decision_id"],
        receipt_hash=receipt["receipt_hash"],
        replay_token=receipt["replay_token"],
        receipt=receipt,
    )
