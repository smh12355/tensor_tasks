from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.action = ActionChains(self.driver)
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def get(self, url):
        return self.driver.get(url)