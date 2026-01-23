import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def test_config_has_crops():
    config = json.loads((BASE_DIR / "config.json").read_text())
    crops = config.get("crops", [])
    assert isinstance(crops, list)
    assert len(crops) > 0


def test_defects_has_catalog():
    defects = json.loads((BASE_DIR / "defects.json").read_text())
    assert "defects" in defects
    assert isinstance(defects["defects"], list)
