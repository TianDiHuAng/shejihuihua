"""根据已写条目同步 coverage.json 的层级、状态、来源数与待核实数。"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    cov_path = ROOT / "coverage.json"
    coverage = json.loads(cov_path.read_text(encoding="utf-8"))
    rows = {r["id"]: r for r in coverage["entries"]}
    written = {}
    for path in sorted((ROOT / "entries").glob("*.json")):
        for entry in json.loads(path.read_text(encoding="utf-8")).get("entries", []):
            written[entry["id"]] = entry
    today = date.today().isoformat()
    for eid, entry in written.items():
        if eid not in rows:
            raise ValueError(f"未登记条目: {eid}")
        row = rows[eid]
        row["level"] = entry.get("level", "L1")
        row["status"] = "已写"
        row["source_count"] = len(entry.get("sources", []))
        row["needs_verification_count"] = 1 if entry.get("needs_verification") else 0
        row["last_updated"] = today
    coverage["updated"] = today
    cov_path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"coverage updated: {len(written)} written / {len(rows)} total")


if __name__ == "__main__":
    main()
