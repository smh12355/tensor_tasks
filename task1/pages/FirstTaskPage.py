from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

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
        return self.find(self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)
