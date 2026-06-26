import pytest
import csv

print("=====================================")
print("      AIRDROP QA TOOLKIT")
print("=====================================\n")

url = input("Enter Website URL (Example: https://base.org): ").strip()

if not (url.startswith("http://") or url.startswith("https://")):
    print("\nInvalid website URL!")
    print("Please enter a full URL.")
    print("Example: https://base.org")
    input("\nPress Enter to exit...")
    exit()

with open("campaigns.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "url"])
    writer.writerow(["Website", url])

print("\nRunning tests...\n")

pytest.main(["tests/", "-q"])

print("\n=====================================")
print("Finished!")
print("Check reports/report.html")
print("=====================================")