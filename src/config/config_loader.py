import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def load(self):
        with open(self.config_path, 'r') as file:
            return json.load(file)
            