import json
import os


class StateManager:
    def __init__(self, state_file):
        self.state_file = state_file
        self._state = {}
        self._load_state()
    
    def _load_state(self):
        self._state = self.load()
    
    def load(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}
    
    def save(self, state):
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        with open(self.state_file, "w") as f:
            json.dump(state, f, indent=2)
        self._state = state
    
    def get(self, key, default=None):
        return self._state.get(key, default)
    
    def set(self, key, value):
        self._state[key] = value
        self.save(self._state)
