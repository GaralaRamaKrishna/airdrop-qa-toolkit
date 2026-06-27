"""
Airdrop QA Toolkit
Entry point for running the toolkit.
"""

print("Debug Mode (Optional)\n")

print("If you're testing wallet interactions:")
print("- Close all Google Chrome windows.")
print("- Start Chrome in Debug Mode.")
print("- Open Command Prompt and run:\n")
print("Copy and paste this command:\n")
print('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\\Google\\Chrome-Debug"\n')

print("- Then run Debug_Mode.bat.\n")

print("Otherwise, simply press Enter to continue.\n")

input("Press Enter to continue...")

import main