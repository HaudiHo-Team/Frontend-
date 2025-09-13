import os
import json
from typing import Dict, Any

class AppConfig:
    def __init__(self):
        self.config = {
            "app": {
                "name": "Frontend App",
                "version": "2.0.0",
                "description": "Современное Streamlit приложение с красивым интерфейсом",
                "author": "Development Team",
            },
            "ui": {
                "theme": "light",
                "language": "ru",
                "page_title": "Frontend App",
                "page_icon": "🚀",
                "layout": "wide",
                "sidebar_state": "expanded",
            },
        }

    def get(self, key: str, default=None):
        node = self.config
        try:
            for k in key.split("."):
                node = node[k]
            return node
        except (KeyError, TypeError):
            return default

    def set(self, key: str, value: Any):
        node = self.config
        keys = key.split(".")
        for k in keys[:-1]:
            node = node.setdefault(k, {})
        node[keys[-1]] = value

    def is_feature_enabled(self, feature: str) -> bool:
        return self.get(f"features.{feature}", False)

    def update_from_env(self):
        env_map = {
            "STREAMLIT_THEME": "ui.theme",
            "STREAMLIT_LANGUAGE": "ui.language",
            "CACHE_TTL": "data.cache_ttl",
            "MAX_FILE_SIZE": "data.max_file_size",
        }
        for env_var, key in env_map.items():
            val = os.getenv(env_var)
            if val is not None:
                if key in ["data.cache_ttl", "data.max_file_size"]:
                    val = int(val)
                self.set(key, val)

    def to_dict(self) -> Dict[str, Any]:
        return self.config.copy()

    def save_to_file(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

    def load_from_file(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    def validate(self) -> bool:
        if not isinstance(self.get("data.cache_ttl"), int) or self.get("data.cache_ttl") <= 0:
            return False
        if not isinstance(self.get("data.max_file_size"), int) or self.get("data.max_file_size") <= 0:
            return False
        return True
