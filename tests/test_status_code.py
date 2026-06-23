import requests
from utils.campaign_reader import get_campaigns
from utils.logger import logger


def test_status_code():

    campaigns = get_campaigns()

    for name, url in campaigns:

        logger.info(f"Checking status code for {name}")

        response = requests.get(url)

        assert response.status_code == 200

        logger.info(f"{name} returned status code 200")