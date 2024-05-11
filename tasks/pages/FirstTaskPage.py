from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time

class FirstTaskPage(BasePage):

    LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH = (
        By.XPATH,
        "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16' and text()='Сила в людях']")
    LOCATOR_FIRST_TASK_LINK_SEARCH = (
        By.XPATH, 
        "//a[@class='tensor_ru-link tensor_ru-Index__link' and @href='/about']")
    LOCATOR_INVISIBILITY_ELEMENT_CLOSE = (
        By.XPATH,
        "//div[@class = 'tensor_ru-CookieAgreement__close icon-Close ws-flex-shrink-0 ws-flexbox ws-align-items-center']"
    )
    
    def FindFirstPhrase(self):
        self.get("https://tensor.ru/")
        data = self.waiter_until(self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)
        return data
    
    def TextLinkOpen(self):
        self.get("https://tensor.ru/")
        link = self.waiter_until(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
        another_link = link.get_attribute('href')
        self.action_click(self.waiter_until(self.LOCATOR_INVISIBILITY_ELEMENT_CLOSE))
        self.action_click(link)
        url = self.url()
        return [another_link, url]