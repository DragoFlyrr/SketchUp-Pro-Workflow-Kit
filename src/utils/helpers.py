"""Utility functions for file handling and validation."""

import json
from pathlib import Path
from typing import Any, Dict


def load_config(config_path: Path) -> Dict[str, Any]:
    """Load JSON configuration file."""
    if not config_path.exists():
        return {}
    return json.loads(config_path.read_text(encoding="utf-8"))


def validate_paths(paths: list) -> list:
    """Validate that all paths exist."""
    existing = []
    for p in paths:
        path = Path(p)
        if path.exists():
            existing.append(path)
    return existing


def ensure_dir(directory: Path) -> Path:
    """Create directory if it doesn't exist."""
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def sanitize_filename(filename: str) -> str:
    """Remove illegal characters from filename."""
    illegal = '<>:"/\\|?*'
    for char in illegal:
        filename = filename.replace(char, "_")
    return filename
