from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 20)
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def find_list(self, locator):
        return self.driver.find_elements(*locator)
    
    def get(self, url):
        return self.driver.get(url)
    
    # def wait(self):
    #     return WebDriverWait(self.driver, self.implicit_wait_timeout)
    
    def url(self):
        return self.driver.current_url
    
    def waiter_until_list(self, locator):
        return self.waiter.until(EC.presence_of_all_elements_located(locator))

    def waiter_until(self, locator):
        return self.waiter.until(EC.presence_of_element_located(locator))
    
    def waiter_new_url(self):
        self.waiter.until(EC.url_changes(self.driver.current_url))
    
    def waiter_clicable(self, locator):
        return self.waiter.until(EC.element_to_be_clickable(locator))
    
    def invisibility_element(self,locator):
        self.waiter.until(EC.invisibility_of_element(locator))