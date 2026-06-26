@echo off
title Airdrop QA Toolkit - Debug Mode
color 0B

echo.
echo ==========================================
echo      Airdrop QA Toolkit - Debug Mode
echo ==========================================
echo.

echo Before continuing:
echo 1. Start Chrome in Debug Mode.
echo 2. Keep Chrome open.
echo 3. Then press any key.
echo.

pause >nul

python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo Python is not installed.
    echo Download it from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit
)

echo Installing required packages...
pip install -r requirements.txt --quiet --disable-pip-version-check

echo.
echo Starting toolkit...
echo.

set DEBUG_MODE=1
python main.py

echo.
echo ==========================================
echo Finished!
echo Report saved in:
echo reports\report.html
echo ==========================================
pause