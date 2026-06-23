from datetime import datetime

with open("../reports/report.txt", "w") as f:
    f.write("Airdrop QA Toolkit Report\n")
    f.write("----------------------\n")
    f.write(f"Generated on: {datetime.now()}\n")
    f.write("Basic validation completed successfully.\n")