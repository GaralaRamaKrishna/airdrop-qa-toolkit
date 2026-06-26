@echo off
title Airdrop QA Toolkit - Single Website
color 0A

echo.
echo ==========================================
echo      AIRDROP QA TOOLKIT
echo ==========================================
echo.

:ask

set /p URL=Enter Website URL (Example: https://base.org):

if "%URL%"=="" (
    echo.
    echo Please enter a website URL.
    echo.
    goto ask
)

echo name,url>campaigns.csv
echo Custom Website,%URL%>>campaigns.csv

echo.
echo Running tests...
echo.

python main.py

pause