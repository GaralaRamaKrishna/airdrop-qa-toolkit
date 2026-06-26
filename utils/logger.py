import logging

# Set up a simple log so we can see what the toolkit is doing while it runs.
# Each line will show the time, the type of message, and the message itself.
# Example: 2024-01-01 12:00:00 - INFO - Opening Bitget Wallet

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()