import json
from pathlib import Path
import unittest

from state_store import StateStore

BASE_DIR = Path(__file__).resolve().parents[1]

class TestConfigLoading(unittest.TestCase):
    def setUp(self):
        self.config_path = BASE_DIR / "config.json"
        self.defects_path = BASE_DIR / "defects.json"

    def test_config_has_crops(self):
        config = json.loads(self.config_path.read_text())
        crops = config.get("crops", [])
        assert isinstance(crops, list), "crops must be a list"
        assert len(crops) > 0, "crops array can't be empty"

    def test_config_includes_onionw(self):
        config = json.loads(self.config_path.read_text())
        crops = config.get("crops", [])
        assert "onionw" in crops, "onionw must be in crops array"

class TestDefectFiltering(unittest.TestCase):
    def setUp(self):
        self.defects_path = BASE_DIR / "defects.json"

    def test_defects_has_catalog(self):
        defects = json.loads(self.defects_path.read_text())
        assert "defects" in defects, "defects key must exist"
        assert isinstance(defects["defects"], list), "defects must be a list"
        assert len(defects["defects"]) > 0, "defects can't be empty"

class TestStateStore(unittest.TestCase):    
    def test_state_store_save_and_get(self):
        store = StateStore()
        
        store.save_state("selected_crop", "potato")
        assert store.get_state("selected_crop") == "potato"
    
    def test_state_store_remove(self):
        store = StateStore()
        
        store.save_state("selected_crop", "potato")
        assert store.get_state("selected_crop") == "potato"

        store.remove_state("selected_crop")
        assert store.get_state("selected_crop") is None