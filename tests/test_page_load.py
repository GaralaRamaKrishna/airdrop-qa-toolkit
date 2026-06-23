
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import logger
from utils.campaign_reader import get_campaigns
from utils.screenshot_helper import take_screenshot
from pages.base_page import BasePage

def test_page_load(driver):

    campaigns = get_campaigns()

    for name, url in campaigns:

        try:

            logger.info(f"Opening {name}")

            page = BasePage(driver)

            page.open_site(url)

            assert page.get_title() is not None

            logger.info(f"{name} loaded successfully")

        except Exception:

            take_screenshot(driver, name)

            raise

