from __future__ import annotations

from state_store import state_store
from ipc import send_selected_crop

def get_available_crops(config: dict) -> list[str]:
    crops = config.get("crops", [])
    return crops

def select_crop(crop: str) -> None:
    state_store.save_state("selected_crop", crop)
    send_selected_crop(crop)

def render_defect_sliders(defects_config: dict) -> list[str]:
    selected_crop = state_store.get_state("selected_crop")
    defects = defects_config.get("defects", [])
    visibility_section = defects_config.get("visibility", {})
    
    visibilities_for_selected_crop = visibility_section.get(selected_crop, {})
    
    sliders = []    
    for defect in defects:
        key = defect.get("key")
        label = defect.get("label")
        status = visibilities_for_selected_crop.get(key, "hidden")
        
        if status in ["visible", "ignore"]:
            sliders.append({
                "label": label,
                "status": status
            })
    
    return sliders
