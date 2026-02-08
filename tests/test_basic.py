"""Basic tests for workflow engine."""

import pytest
from pathlib import Path
from src.core.engine import WorkflowEngine
from src.utils.helpers import sanitize_filename, ensure_dir


def test_engine_init():
    """Test engine initialization."""
    engine = WorkflowEngine()
    assert engine.supported_formats == ["obj", "fbx", "dae", "stl"]


def test_sanitize_filename():
    """Test filename sanitization."""
    dirty = 'file<>:"/\\|?*name.txt'
    clean = sanitize_filename(dirty)
    assert '<' not in clean
    assert '>' not in clean
    assert '_' in clean


def test_ensure_dir(tmp_path):
    """Test directory creation."""
    test_dir = tmp_path / "test_subdir"
    result = ensure_dir(test_dir)
    assert result.exists()


def test_engine_backup(tmp_path):
    """Test backup creation."""
    engine = WorkflowEngine()
    backup = engine.create_backup("TestProject", tmp_path)
    assert backup.exists()
    assert "TestProject" in backup.name
