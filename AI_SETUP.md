# AI Setup Guide — Airdrop QA Toolkit

This guide is for beginners.

If you get stuck while setting up the toolkit, copy everything below into ChatGPT and let it guide you step by step.

---

## How to use

1. Open https://chatgpt.com/ or any ai.
2. Copy everything below this line.
3. Paste it into ChatGPT.
4. Follow the instructions one step at a time.

---

Hi ChatGPT,

I downloaded **Airdrop QA Toolkit** from GitHub.

I have never used Python or Command Prompt before.

Please help me set up and run this toolkit on my Windows computer.

### Important

* Explain everything in simple English.
* Guide me one step at a time.
* Wait for me to confirm each step before continuing.
* If I get an error, help me fix it before moving on.
* Assume nothing is already installed.

### Help me with:

1. Check if Python is installed.
2. Help me install Python if needed.
3. Make sure **"Add Python to PATH"** is enabled.
4. Help me open the project folder.
5. Help me run **Start_Toolkit.bat**.
6. If I get an error, explain it in simple English and help me fix it.
7. Help me edit **campaigns.csv** to add my own websites.
8. Explain the HTML report after the scan finishes.

### Common Errors

**python is not recognized**

Python is not installed or PATH is not configured correctly.

**pip is not recognized**

Python was installed but PATH was not configured correctly.

**No module named ...**

Install the missing package.

**FileNotFoundError**

The file or folder cannot be found.

**ChromeDriver errors**

Help me update Google Chrome and ChromeDriver.

For every error:

* Explain what happened in one simple sentence.
* Give me the exact steps to fix it.

My goal is to successfully run the toolkit and test my Web3 campaign websites.

Thank you!

---

# Manual Setup (Optional)

## 1. Install Python

Download Python:

https://www.python.org/downloads/

During installation, enable:

✔ Add Python to PATH

---

## 2. Install Required Packages

Open **Command Prompt** inside the project folder and run:

```
pip install -r requirements.txt
```

---

## 3. Start the Toolkit

For most users:

* Double-click **Start_Toolkit.bat**

Advanced users can also run:

```
python airdrop_auto.py
```

---

## 4. Chrome Debug Mode (Optional)

Use this mode only if you want to test wallet interactions.

### Step 1

Close **all Google Chrome windows**.

This is important before starting Chrome in Debug Mode.

### Step 2

Open **Command Prompt**.

### Step 3

Copy and paste the command below, then press **Enter**.

```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="%LOCALAPPDATA%\Google\Chrome-Debug"
```

A new Chrome window will open in Debug Mode.

### Step 4

Double-click:

```
Debug_Mode.bat
```

The toolkit will connect to the Debug Chrome window.

Note:

Only use Debug Mode for testing.
Do not use it for personal browsing or logging into sensitive accounts.

---

## Still Need Help?

If the toolkit still doesn't work, create a GitHub Issue and include:

* Windows version
* Python version
* What happened
* A screenshot of the error

This helps improve the toolkit for everyone.
