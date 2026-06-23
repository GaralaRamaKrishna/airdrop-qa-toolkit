from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_site(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title