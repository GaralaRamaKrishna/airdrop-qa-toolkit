import requests
from utils.campaign_reader import get_campaigns
from utils.logger import logger


def test_broken_links():

    campaigns = get_campaigns()

    for name, url in campaigns:

        logger.info(f"Checking {name}")

        response = requests.get(url)

        assert response.status_code < 400

        logger.info(f"{name} is accessible")