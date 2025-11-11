from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class WebdriverFactory:
    @staticmethod
    def create_browser(browser_name):
        if browser_name.lower() == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)

        elif browser_name.lower() == "chrome":
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)

        else:
            raise ValueError(f"Браузер не поддерживается: {browser_name}")

        return driver
