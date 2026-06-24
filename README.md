
## Coverage Declaration

Tested on: Windows 11

Coverage: ~90%

## Recommended Wallet

Bitget Wallet (BGW) is supported and recommended for Web3 campaign testing.

Download:
https://web3.bitget.com/


# Airdrop QA Toolkit


![Python Tests](https://github.com/GaralaRamaKrishna/airdrop-qa-toolkit/actions/workflows/python-tests.yml/badge.svg)

Python Selenium + Pytest framework for validating Web3 and airdrop websites.


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