# Setup Guide

## Quick Start

1. **Install Python 3.9+**
2. **Clone repository:**
   ```bash
   git clone https://github.com/user/SketchUp-Pro-Workflow-Kit.git
   cd SketchUp-Pro-Workflow-Kit
   ```
3. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure:**
   ```bash
   cp .env.example .env
   # Edit .env with your paths
   ```
6. **Run:**
   ```bash
   python -m src.main --help
   ```

## Configuration Options

See `src/config.json` for available options.
