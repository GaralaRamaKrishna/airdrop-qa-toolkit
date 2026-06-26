# Frequently Asked Questions

---

## Python is not installed

Download Python from:

https://www.python.org/downloads/

During installation, tick the box that says **"Add Python to PATH"** before clicking Install.

---

## Chrome doesn't open

Make sure Google Chrome is installed on your computer.

Download it from:

https://www.google.com/chrome/

---

## Tests fail

First, check your internet connection. The toolkit needs to reach each campaign URL to run checks.

If the internet is fine, one of the campaign websites may be temporarily down. That is normal — just try again later.

---

## Bitget Wallet isn't detected

The default mode runs Chrome without extensions. This is expected.

To test with your wallet installed, see **CHROME_DEBUG.md** for how to connect the toolkit to your existing Chrome window.

---

## Where do I add my own campaign URLs?

Open **`campaigns.csv`** in any text editor (Notepad works fine).

Replace the example URLs with your own, one per line:

```
name,url
My Campaign,https://yourcampaign.com
Another Project,https://anotherproject.xyz
```

Save the file and run the toolkit again.

---

## The toolkit ran but I don't see a report

Check the **`reports/`** folder inside the project.

Open `report.html` in your browser (double-click it).

---

## I get a "pip is not recognized" error

This usually means Python was installed without the PATH option.

Uninstall Python, then reinstall it and make sure to tick **"Add Python to PATH"** during setup.

---

## Something else went wrong

Open **`AI_SETUP.md`**, copy everything in it, and paste it into [ChatGPT](https://chatgpt.com/).

The AI will walk you through setup step by step in plain English.

---

## I want to report a bug or suggest something

Open a GitHub Issue on the project page and include:

- Your Windows version
- What happened
- A screenshot of any error message

Every piece of feedback helps improve the toolkit for the whole community.
