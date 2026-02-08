#!/bin/bash
# Deployment script for SketchUp Workflow Kit

set -e

echo "🚀 Deploying SketchUp Workflow Kit..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run tests
echo "🧪 Running tests..."
pytest tests/ -v

# Build package
echo "🔨 Building package..."
python setup.py sdist bdist_wheel

echo "✅ Deployment complete!"
