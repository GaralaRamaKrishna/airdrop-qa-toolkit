# Airdrop QA Toolkit

A simple Python toolkit to check Web3 websites before connecting your wallet.

No coding required. Install Python once, then run the toolkit.

---

## Features

* Check website availability
* Verify HTTPS / SSL certificate
* Check HTTP status code
* Detect redirects
* Measure page load speed
* Verify wallet button
* Check social links
* Generate an HTML report
* Save screenshots if a test fails

---

## Requirements

* Windows 10 or Windows 11
* Python 3.10 or later
* Google Chrome
* Internet connection

---

## Setup

### 1. Download the project

Download or clone this repository.

### 2. Install Python

Download Python:

https://www.python.org/downloads/

During installation, make sure you enable:

**✔ Add Python to PATH**

---

## Run

### Test One Website

Double-click:

**Test_One_Website.bat**

Enter a website URL when prompted.

Example:

```
https://base.org
```

---

### Test Multiple Websites

Open **campaigns.csv** and add your websites.

Example:

```csv
name,url
Base,https://base.org
Bitget,https://web3.bitget.com
```

Save the file.

Then double-click:

**Start_Toolkit.bat**

---

## Run from Command Prompt (Optional)

For advanced users:

1. Open Command Prompt.
2. Open the project folder.
3. Run:

```
python airdrop_auto.py
```

---

## Manual Installation (Optional)

If the required packages are not installed, open Command Prompt in the project folder and run:

```
pip install -r requirements.txt
```

---

## Debug Mode (Optional)

Debug Mode is only required for wallet interaction testing.

1. Close all Google Chrome windows.
2. Open Command Prompt.
3. Copy and paste this command:

```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"
```

4. Then run:

**Debug_Mode.bat**

**Note:** Keep the Debug Chrome window open until testing finishes.

---

## Reports

After the scan finishes, open:

```
reports/report.html
```

If a test fails, screenshots are saved inside the **screenshots** folder.

---

## Need Help?

See:

* **FAQ.md**
* **AI_SETUP.md**

---

## Screenshots

### Start Toolkit

![Start Toolkit](screenshots/start_toolkit.png)

### Test Results

![Test Results](screenshots/test_results.png)

### HTML Report

![HTML Report](screenshots/html_report.png)

### Project Structure

![project_structure.png](screenshots/project_structure.png)
---

## Coverage Declaration

Tested on: Windows

Coverage: ~100%

---

## License

MIT License
