import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    use_debug = os.getenv("DEBUG_MODE") == "1"

    options = Options()

    if use_debug:
        # Connect to an already running Chrome
        options.add_experimental_option(
            "debuggerAddress",
            "127.0.0.1:9222"
        )
    else:
        # Start a fresh headless Chrome
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver

    # Don't close the user's Chrome in debug mode
    if not use_debug:
        driver.quit()