from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import logging

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.implicit_wait_timeout = 20
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def find_list(self, locator):
        return self.driver.find_elements(*locator)
    
    def get(self, url):
        return self.driver.get(url)
    
    def wait(self):
        return self.driver.implicitly_wait(self.implicit_wait_timeout)
    
    def url(self):
        return self.driver.current_url