# Airdrop QA Toolkit

A Python-based QA automation toolkit built to validate Web3 campaign pages and practice Selenium automation.

## Features

- Selenium WebDriver
- Pytest framework
- Logging support
- HTML reports
- CSV-driven tests
- Screenshot capture on failures
- Page Object Model (POM)
- Config management

## Tech Stack

- Python
- Selenium
- Pytest
- Pandas
- WebDriver Manager

## Project Structure

```
airdrop-qa-toolkit
├── config
├── pages
├── reports
├── screenshots
├── tests
├── utils
├── campaigns.csv
├── requirements.txt
└── README.md
```

## Run Tests

```bash
pytest tests/ -v -s
```

## Generate HTML Report

```bash
pytest tests/ --html=reports/report.html
```

This project is being continuously improved as part of learning QA Automation.