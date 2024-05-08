from selenium.webdriver.common.by import By
class Base:

    def __init__(self, driver, base_url = "https://tensor.ru/") -> None:
        self.driver = driver
        self.base_url = base_url

class TaskSolver(Base):

    LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH = (By.XPATH, "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16' and text()='Сила в людях']")
    LOCATOR_FIRST_TASK_LINK_SEARCH = (By.XPATH, "//a[@class='tensor_ru-link tensor_ru-Index__link' and text()='Подробнее' and @href='/about']")
    LOCATOR_FIRST_TASK_IMG_SEARCH = (By.CLASS_NAME, "tensor_ru-About__block3-image-filter")

    def FirstPhraseCheck(self):
        return self.driver.find_element(*self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)
