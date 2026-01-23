from __future__ import annotations

from state import GLOBAL_D
from ipc import send_selected_crop

# Legacy hardcoded defect labels (bad)
DEFECT_LABELS = [
    "rot", "green", "bruise", "skin", "sprout",
    "size_small", "size_large", "shape", "damage", "other",
]

# Legacy visible defects (bad)
VISIBLE_DEFECTS = {"rot", "green", "bruise", "sprout"}


def get_available_crops(config: dict) -> list[str]:
    crops = config.get("crops", [])
    # Legacy customer hardcode (bad)
    if GLOBAL_D.get("customer") == "meijer":
        return ["potato"]
    return crops


def select_crop(crop: str) -> None:
    GLOBAL_D["selected_crop"] = crop
    send_selected_crop(crop)


def render_defect_sliders() -> list[str]:
    # Legacy: ignores per-crop defect visibility config
    sliders = []
    for label in DEFECT_LABELS:
        if label in VISIBLE_DEFECTS:
            sliders.append(label)
    return sliders
