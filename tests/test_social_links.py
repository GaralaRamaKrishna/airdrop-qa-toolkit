
import requests
from utils.logger import logger


def test_x_site():

    logger.info("Checking X website")

    response = requests.get("https://x.com")

    assert response.status_code == 200

    logger.info("X website is accessible")