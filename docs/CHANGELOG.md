# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2025-02-08

### Added
- Batch export support for .dae (Collada) format
- Improved memory handling for large models (>100MB)
- New `report` command for library statistics
- Windows path encoding fixes for non-ASCII characters

### Changed
- Updated default quality preset to "high"
- Refactored backup naming convention

### Fixed
- Issue with nested directory exports
- Memory leak in validation loop

## [2.0.0] - 2025-01-15

### Added
- Complete refactor to Typer CLI framework
- JSON schema validation for config files
- Plugin system for custom exporters
- Rich console output with progress bars
- Parallel processing support (multithreading)

### Changed
- Breaking: Config format v1 → v2
- Breaking: CLI commands renamed for consistency

### Removed
- Legacy argparse interface
- Python 3.8 support

## [1.5.0] - 2024-12-10

### Added
- Initial backup automation
- Basic export functionality
- Geometry validation core
