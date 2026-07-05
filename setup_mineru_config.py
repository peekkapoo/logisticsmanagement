import json
import os

home_dir = os.path.expanduser("~")
config_path = os.path.join(home_dir, "magic-pdf.json")

config_data = {
    "models-dir": "d:/LogManagement/.agents/skills/professional-writing/models/mineru_models",
    "device-mode": "cpu",
    "layout-config": {
        "model": "doclayout_yolo"
    },
    "formula-config": {
        "mfd_model": "yolov8m_mfd",
        "mfr_model": "UniMERNet",
        "enable": True
    },
    "table-config": {
        "model": "rapid_table",
        "enable": False,
        "max_time": 400
    }
}

# If config already exists, update it instead of replacing entirely
if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        try:
            existing = json.load(f)
            existing.update(config_data)
            config_data = existing
        except json.JSONDecodeError:
            pass

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=4)

print(f"MinerU config written to {config_path}")
