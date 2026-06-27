@echo off
title Airdrop QA Toolkit - Debug Mode
color 0B

echo.
echo ==========================================
echo      Airdrop QA Toolkit - Debug Mode
echo ==========================================
echo.

echo This mode is for testing wallet interactions.
echo.
echo Before continuing:
echo.
echo 1. Close ALL Google Chrome windows.
echo 2. Press any key.
echo 3. Chrome will open automatically in Debug Mode.
echo 4. Keep the Debug Chrome window OPEN until testing finishes.
echo.
echo Do NOT use Debug Chrome for personal browsing or log into sensitive accounts.
echo A temporary Chrome profile will be used.
echo.

pause

echo.
echo Starting Google Chrome in Debug Mode...
echo.

start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"

timeout /t 3 >nul

echo.
echo Google Chrome started successfully.
echo Please keep this browser window open while the toolkit is running.
echo.

python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo Python is not installed.
    echo.
    echo Download Python from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit
)

echo.
echo Installing required packages...
pip install -r requirements.txt --quiet --disable-pip-version-check

echo.
echo Starting Airdrop QA Toolkit...
echo.

set DEBUG_MODE=1
python main.py

echo.
echo ==========================================
echo Testing completed.
echo.
echo Report saved in:
echo reports\report.html
echo.
echo You can now close the Debug Chrome window.
echo ==========================================
pause