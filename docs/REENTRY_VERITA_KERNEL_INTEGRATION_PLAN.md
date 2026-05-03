# Reentry VERITA Kernel Integration Plan

## Status

A private reentry-governance kernel exists as protected build material.

It must not be copied into this public repository.

The public repository remains a bounded proof surface for stage admission, not a flight controller, vehicle model, reentry trajectory system, propulsion system, thermal protection design tool, fabrication tool, or aerospace deployment package.

## Integration posture

Correct posture:

```text
Private reentry kernel informs public stage-admission proof behavior.
The public repo exposes only safe surrogate outcomes, receipts, and no-advance invariant proof.
```

Incorrect posture:

```text
Publishing reentry dynamics, guidance behavior, vehicle parameters, thermal model internals, or production kernel logic.
```

## Private kernel role

The protected kernel may be used internally as a reference source for:

- reentry-stage safety posture
- thermal-margin pressure language
- capacity/margin reasoning
- permit/veto analogy
- ledger/receipt continuity
- fail-closed stage admission

It must not be used publicly to expose:

- trajectory logic
- guidance logic
- vehicle-specific parameters
- thermal protection design
- aerospace operational procedures
- export-controlled technical detail
- production control substrate

## Public abstraction layer

The public mission-control repo should expose only this abstraction:

```text
reentry formation request
→ safety standing check
→ evidence continuity check
→ witness standing check
→ monotone phase movement check
→ integrity check
→ stage outcome
→ receipt
→ replay token
```

## Reentry-specific proof invariant

```text
No reentry-stage formation may advance unless safety standing, evidence continuity, witness standing, monotone phase movement, integrity, receipt, and replay basis hold.
```

## Public route mapping

```text
POST /mission/resolve      general mission-stage resolution
POST /stage/advance        bounded stage advancement request
POST /simulation/admit     simulation admission gate
POST /claim/attempt        controlled claim-stage attempt
```

Future safe public route, if needed:

```text
POST /reentry/stage/admit
```

This route should remain surrogate-only.

## Public outcome mapping

```text
ADMIT       stage advancement permitted
HOLD        margin/evidence unresolved; no advancement
REBOUND     return to prior valid mission state
REFUSE      lacks standing; no advancement
HALT        safety/integrity failure; stop corridor
QUARANTINE  contaminated formation isolated
CERTIFY     bounded proof packet ready for controlled review
```

## Receipt expectation

Public receipts should carry proof of stage posture, not sensitive aerospace mechanics:

```text
mission_decision_id
corridor_id
stage_from
stage_to
candidate_hash
policy_hash
witness_hash
outcome
reason_code
advanced
invariant_holds
receipt_hash
replay_token
```

## NASA-facing review language

Use:

```text
reentry-facing stage-admission proof surface
controlled mission-stage evaluation corridor
public surrogate proof harness
private kernel protected/not included
```

Do not use:

```text
reentry controller
flight guidance
NASA approved
flight ready
thermal protection design
trajectory design
production aerospace deployment
```

## Clean external line

```text
This is not a reentry controller.

It is a reentry-facing stage-admission proof surface showing that invalid AI-assisted mission formations cannot advance without safety, standing, monotonicity, receipt, and replay.
```
