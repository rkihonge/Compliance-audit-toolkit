import yaml
from pathlib import Path
from report import generate_report

CHECKLIST_PATH = Path(__file__).parent.parent / "data/audit_checklist.yml"
OUTPUT_PATH = Path(__file__).parent.parent / "output/audit_results.md"

def run_audit():
    with open(CHECKLIST_PATH, "r") as f:
        checklist = yaml.safe_load(f)

    results = []
    print("Compliance Audit Started:\n")
    for control in checklist["controls"]:
        answer = input(f"[{control['id']}] {control['name']} - {control['description']} (Compliant/Non-Compliant): ")
        results.append({"id": control["id"], "name": control["name"], "status": answer})

    generate_report(results, OUTPUT_PATH)
    print(f"\n✅ Audit complete. Report saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    run_audit()
