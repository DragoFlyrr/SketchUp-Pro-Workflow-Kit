"""Basic usage example for SketchUp Workflow Kit."""

from pathlib import Path
from src.core.engine import WorkflowEngine

# Initialize engine
engine = WorkflowEngine(config_path=Path("config.json"))

# Validate a model
model_path = Path("data/sample_house.skp")
report = engine.validate(model_path, strict=True)

print(f"Validation report: {report['output_path']}")
print(f"Issues found: {report['issues']}")

# Create backup
backup_path = engine.create_backup("MyProject")
print(f"Backup created at: {backup_path}")
