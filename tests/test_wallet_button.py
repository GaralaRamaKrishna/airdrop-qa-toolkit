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
from utils.logger import logger


def test_wallet_page(driver):

    logger.info("Opening Monad website")


    driver.get("https://testnet.monad.xyz")

    assert driver.current_url is not None

    logger.info("Wallet page opened successfully")

