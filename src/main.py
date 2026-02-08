#!/usr/bin/env python3
"""
SketchUp Pro Workflow Kit - CLI Entry Point

Professional automation utilities for 3D modeling pipelines.
Handles geometry validation, batch exports, and model optimization.
"""

import json
import sys
from pathlib import Path
from typing import Optional

import typer
from rich import print as rprint
from rich.console import Console

from src.core.engine import WorkflowEngine
from src.utils.helpers import load_config, validate_paths

app = typer.Typer(
    name="skp-kit",
    help="Workflow automation for 3D modeling pipelines",
    add_completion=False,
)
console = Console()


@app.command()
def validate(
    file: Path = typer.Option(..., "--file", "-f", help="Path to .skp or .json descriptor"),
    strict: bool = typer.Option(False, "--strict", help="Enable strict validation mode"),
):
    """Run geometry validation checks on model file."""
    if not file.exists():
        rprint("[red]Error:[/red] File not found")
        sys.exit(1)
    
    engine = WorkflowEngine()
    report = engine.validate(file, strict=strict)
    
    rprint(f"[green]✓ Validation complete[/green]")
    rprint(f"  Issues found: {report['issues']}")
    rprint(f"  Report saved: {report['output_path']}")


@app.command()
def export(
    directory: Path = typer.Option(..., "--dir", "-d", help="Source directory"),
    format: str = typer.Option("obj", "--format", help="Export format (obj, fbx, dae)"),
    out: Path = typer.Option(Path("./exports"), "--out", "-o"),
):
    """Batch export models with specified format."""
    engine = WorkflowEngine()
    results = engine.batch_export(directory, format, out)
    rprint(f"[cyan]📦 Exported {len(results)} files to {out}[/cyan]")


@app.command()
def backup(
    project: str = typer.Option(..., "--project", "-p", help="Project name"),
    dest: Optional[Path] = typer.Option(None, "--dest", help="Backup destination"),
):
    """Create timestamped backup of project directory."""
    engine = WorkflowEngine()
    backup_path = engine.create_backup(project, dest)
    rprint(f"[blue]💾 Backup created:[/blue] {backup_path}")


if __name__ == "__main__":
    app()
