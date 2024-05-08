from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import requests

class FirstTaskPage(BasePage):

    LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH = (
        By.XPATH,
        "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16' and text()='Сила в людях']")
    LOCATOR_FIRST_TASK_LINK_SEARCH = (
        By.XPATH, 
        "//a[@class='tensor_ru-link tensor_ru-Index__link' and text()='Подробнее' and @href='/about']")
    LOCATOR_FIRST_TASK_IMG_SEARCH = (
        By.CLASS_NAME, 
        "tensor_ru-About__block3-image-filter")

    def FindFirstPhrase(self):
        self.get("https://tensor.ru/")
        self.wait()
        return self.find(self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)

    def TextLinkOpen(self):
        self.get("https://tensor.ru/")
        self.wait()
        link = self.find(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
        # print(link.get_attribute('href'))
        r = requests.head(link.get_attribute('href'),timeout=10)
        # r = requests.head("https://tensor.ru/",timeout=10)
        # r = requests.head("https://dzen.ru")
        # self.get("https://dzen.ru")
        # r = requests.head("https://tensor.ru/",timeout=10)
        # print(r)
        # print(r.status_code)
        return r.status_code
    
    def SizeOfPictures(self):
        self.get("https://tensor.ru/about")
        self.wait()
        data = self.find_list(self.LOCATOR_FIRST_TASK_IMG_SEARCH)