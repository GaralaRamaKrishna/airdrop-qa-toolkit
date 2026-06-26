from selenium.webdriver.common.by import By


class BasePage:
    """
    A simple helper for opening websites and reading basic information from them.

    Every check in the tests/ folder uses this to open campaign pages in Chrome.
    """

    def __init__(self, driver):
        # Store the Chrome browser so we can control it
        self.driver = driver

    def open_site(self, url):
        """Open a website in Chrome."""
        self.driver.get(url)

    def get_title(self):
        """Return the title of the page currently open in Chrome."""
        return self.driver.title