@echo off
title Airdrop QA Toolkit
color 0A

echo.
echo  ==========================================
echo        Airdrop QA Toolkit
echo  ==========================================
echo.

echo  Checking Python...
python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo  Python is not installed.
    echo  Please download and install it from:
    echo  https://www.python.org/downloads/
    echo.
    echo  During installation, tick the box that says:
    echo  "Add Python to PATH"
    echo.
    pause
    exit
)

echo  Python found.
echo.

echo  Installing required files...
pip install -r requirements.txt --quiet --disable-pip-version-check
echo.

echo  Starting toolkit...
echo.
python main.py

echo.
echo  ==========================================
echo  Done! Check the reports/ folder for
echo  your results.
echo  ==========================================
echo.
pause
