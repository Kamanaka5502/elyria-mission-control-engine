import argparse
import json
from pathlib import Path

from app.engine import resolve_mission
from app.models import MissionRequest

CASES = {
    "admit_simulation": "admit_simulation.json",
    "refuse_no_witness": "refuse_no_witness.json",
    "halt_safety_failed": "halt_safety_failed.json",
    "rebound_non_monotone": "rebound_non_monotone.json",
    "quarantine_contaminated": "quarantine_contaminated.json",
}


def load_case(case_id: str) -> MissionRequest:
    path = Path("examples") / CASES[case_id]
    return MissionRequest(**json.loads(path.read_text()))


def run_case(case_id: str) -> dict:
    response = resolve_mission(load_case(case_id))
    allowed = response.outcome.value in {"ADMIT", "CERTIFY"}
    passed = response.advanced == allowed and response.invariant_holds is True
    return {
        "case_id": case_id,
        "outcome": response.outcome.value,
        "advanced": response.advanced,
        "invariant_holds": response.invariant_holds,
        "pass": passed,
        "receipt": response.receipt,
    }


def print_case(result: dict) -> None:
    print(f"CASE {result['case_id']}")
    print(f"outcome={result['outcome']}")
    print(f"advanced={str(result['advanced']).lower()}")
    print(f"invariant_holds={str(result['invariant_holds']).lower()}")
    print("PASS" if result["pass"] else "FAIL")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Elyria mission-control invariant proof cases.")
    parser.add_argument("--case", default="all", choices=["all", *CASES.keys()])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    selected = list(CASES.keys()) if args.case == "all" else [args.case]
    results = [run_case(case_id) for case_id in selected]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            print_case(result)
        if all(r["pass"] for r in results):
            print("OVERALL: MISSION_CONTROL_INVARIANT_HOLDS")
        else:
            print("OVERALL: MISSION_CONTROL_INVARIANT_FAILED")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
