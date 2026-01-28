from abc import ABC, abstractmethod
import threading
from typing import Any

class IStateStore(ABC):
    @abstractmethod
    def save_state(self, key: str, value: Any) -> None:
        pass
    
    @abstractmethod
    def get_state(self, key: str) -> Any:
        pass
    
    @abstractmethod
    def remove_state(self, key: str) -> None:
        pass

class StateStore(IStateStore):
    def __init__(self):
        self._store: dict[str, Any] = {}
        self._lock = threading.RLock()

    def save_state(self, key: str, value: Any) -> None:
        with self._lock:
            self._store[key] = value

    def get_state(self, key: str) -> Any:
        with self._lock:
            return self._store.get(key, None)

    def remove_state(self, key: str) -> None:
        with self._lock:
            if key in self._store:
                del self._store[key]

state_store = StateStore()