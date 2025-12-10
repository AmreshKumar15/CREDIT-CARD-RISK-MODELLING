#!/bin/bash

# Lauki Finance - Streamlit App Setup Script
# This script sets up the development environment and runs the app

echo "================================"
echo "🚀 Lauki Finance Setup Script"
echo "================================"
echo ""

# Check Python installation
echo "✓ Checking Python installation..."
python --version

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "✓ Creating virtual environment..."
    python -m venv venv
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
echo "✓ Installing dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "================================"
echo "✅ Setup Complete!"
echo "================================"
echo ""
echo "To run the application, execute:"
echo "  streamlit run main.py"
echo ""
echo "Then open http://localhost:8501 in your browser"
echo ""
