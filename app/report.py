import json
from datetime import datetime, timezone
from pathlib import Path

def build_report():
    data = {"generated_at": datetime.now(timezone.utc).isoformat(),
            "services": [{"name": "api", "status": "healthy"}, {"name": "worker", "status": "healthy"}]}
    Path("output").mkdir(exist_ok=True)
    Path("output/report.json").write_text(json.dumps(data, indent=2) + "\n")
    print("Wrote output/report.json")

if __name__ == "__main__":
    build_report()
