# Client Demo Script

## Objective

Demonstrate one aerospace-facing invariant in a bounded, inspectable corridor:

```text
No unsafe, unwitnessed, non-monotone, contaminated, or invalid engineering formation may advance stages.
```

## Correct Framing

This is a controlled evaluation proof surface.

It is not a rocket design package.
It is not a flight-ready system.
It is not NASA approved or NASA certified.
It does not expose protected scientific, aerospace, fabrication, or production internals.

## Demo Flow

1. Open the repository README.
2. State the invariant.
3. Show the controlled corridor:

```text
Design Note → Simulation Admission Request → Controlled Review → Certification Packet
```

4. Run the proof command:

```bash
python -m app.prove --case all
```

5. Show `admit_simulation`.
   - Expected outcome: `ADMIT`
   - Expected advancement: `true`

6. Show `refuse_no_witness`.
   - Expected outcome: `REFUSE`
   - Expected advancement: `false`

7. Show `halt_safety_failed`.
   - Expected outcome: `HALT`
   - Expected advancement: `false`

8. Show `rebound_non_monotone`.
   - Expected outcome: `REBOUND`
   - Expected advancement: `false`

9. Show `quarantine_contaminated`.
   - Expected outcome: `QUARANTINE`
   - Expected advancement: `false`

10. Confirm final proof line:

```text
OVERALL: MISSION_CONTROL_INVARIANT_HOLDS
```

## Receipt Inspection

For each case, inspect receipt fields:

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

## Client Explanation

The client does not need to trust a claim.

They can inspect the proof surface, run the proof command, and verify that invalid formations do not advance stages.

The point is not that the AI generated an aerospace concept.

The point is that invalid AI-generated engineering formation cannot advance toward simulation, certification, fabrication, or consequence.
