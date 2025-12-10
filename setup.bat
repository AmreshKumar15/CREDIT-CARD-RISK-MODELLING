@echo off
REM Lauki Finance - Streamlit App Setup Script (Windows)
REM This script sets up the development environment and runs the app

echo ================================
echo 🚀 Lauki Finance Setup Script
echo ================================
echo.

REM Check Python installation
echo ✓ Checking Python installation...
python --version

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo ✓ Creating virtual environment...
    python -m venv venv
) else (
    echo ✓ Virtual environment already exists
)

REM Activate virtual environment
echo ✓ Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo ✓ Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo ================================
echo ✅ Setup Complete!
echo ================================
echo.
echo To run the application, execute:
echo   streamlit run main.py
echo.
echo Then open http://localhost:8501 in your browser
echo.
pause
