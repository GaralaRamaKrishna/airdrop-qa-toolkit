import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from utils.campaign_reader import get_campaigns
from utils.logger import logger


def test_title_validation(driver):

    page = BasePage(driver)

    campaigns = get_campaigns()

    for name, url in campaigns:

        logger.info(f"Checking title for {name}")

        page.open_site(url)

        title = page.get_title()

        assert title != ""

