import json 
from pathlib import Path

class ProfileLoader:
    """
    Loads column mappings for a specific CMS/plugin.
    """

    @staticmethod

    def load(profile_name:str):
        profile = Path(f"config/profiles/{profile_name}.json")

        with open(profile, encoding="utf-8") as file:
            return json.load(file)


