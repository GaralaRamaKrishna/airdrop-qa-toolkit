import requests
import time
from utils.campaign_reader import get_campaigns
from utils.logger import logger


def test_response_time():

    campaigns = get_campaigns()

    for name, url in campaigns:

        start = time.time()

        response = requests.get(url)

        end = time.time()

        response_time = end - start

        logger.info(f"{name} response time: {response_time:.2f} seconds")

        assert response.status_code == 200