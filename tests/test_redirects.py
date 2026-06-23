import requests
from utils.campaign_reader import get_campaigns
from utils.logger import logger


def test_redirects():

    campaigns = get_campaigns()

    for name, url in campaigns:

        logger.info(f"Checking redirects for {name}")

        response = requests.get(url, allow_redirects=True)

        final_url = response.url

        logger.info(f"{name} redirected to {final_url}")

        assert final_url.startswith("https://")