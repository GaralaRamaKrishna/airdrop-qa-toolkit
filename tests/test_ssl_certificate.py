import requests
from utils.campaign_reader import get_campaigns
from utils.logger import logger


def test_ssl_certificate():

    campaigns = get_campaigns()

    for name, url in campaigns:

        logger.info(f"Checking SSL for {name}")

        response = requests.get(url, verify=True)

        assert response.status_code == 200

        logger.info(f"{name} SSL certificate is valid")