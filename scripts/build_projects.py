
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
OUTPUT = ROOT / "projects.json"
ALLOWED = {"game", "tool", "app", "software"}
items = []

if PROJECTS.exists():
    for metadata in sorted(PROJECTS.glob("*/project.json")):
        try:
            data = json.loads(metadata.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"Skipping invalid {metadata}: {exc}")
            continue

        name = str(data.get("name", "")).strip()
        description = str(data.get("description", "")).strip()
        category = str(data.get("category", "app")).strip().lower()

        if not name or not description or category not in ALLOWED:
            print(f"Skipping {metadata}: name, description and category are required")
            continue

        folder = metadata.parent.relative_to(ROOT).as_posix()
        image = str(data.get("image", "")).strip()

        if image and not image.startswith(("https://", "http://", "/")):
            image = f"{folder}/{image.lstrip('./')}"

        items.append({
            "name": name,
            "category": category,
            "description": description,
            "image": image,
            "features": data.get("features", [])
                if isinstance(data.get("features", []), list) else [],
            "openUrl": str(data.get("openUrl", "")).strip(),
            "downloadUrl": str(data.get("downloadUrl", "")).strip()
        })

OUTPUT.write_text(
    json.dumps(items, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)
print(f"Wrote {len(items)} B.NOVA projects to {OUTPUT}")
