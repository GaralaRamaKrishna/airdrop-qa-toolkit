@echo off
title Airdrop QA Toolkit - Single Website
color 0A

echo.
echo ==========================================
echo           AIRDROP QA TOOLKIT
echo ==========================================
echo.

python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo Python is not installed.
    echo.
    echo Download Python from:
    echo https://www.python.org/downloads/
    echo.
    echo During installation, make sure you enable:
    echo [✓] Add Python to PATH
    echo.
    pause
    exit
)

python main.py


pause