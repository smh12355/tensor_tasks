from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class FirstTaskPage(BasePage):

    LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH = (
        By.XPATH,
        "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16' and text()='Сила в людях']")
    LOCATOR_FIRST_TASK_LINK_SEARCH = (
        By.XPATH, 
        "//a[@class='tensor_ru-link tensor_ru-Index__link' and text()='Подробнее' and @href='/about']")

    def FindFirstPhrase(self):
        self.get("https://tensor.ru/")
        self.wait()
        return self.find(self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)
    
    def TextLinkOpen(self):
        self.get("https://tensor.ru/")
        self.wait()
        link = self.find(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
        # another_link = "https://oleg.ru/"
        another_link = link.get_attribute('href')
        new = self.get(another_link)
        # new = self.get("https://oleg.ru/")
        self.wait()
        url = self.url()
        return [new, another_link, url]