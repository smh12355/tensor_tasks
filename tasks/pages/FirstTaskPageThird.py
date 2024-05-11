from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class FirstTaskPageThird(BasePage):

    LOCATOR_FIRST_TASK_IMG_SEARCH = (
        By.XPATH, 
        "//div[@class='tensor_ru-About__block3-image-filter']//preceding-sibling::img")

    def SizeOfPictures(self):
        self.get("https://tensor.ru/about")
        # data = self.find_list(self.LOCATOR_FIRST_TASK_IMG_SEARCH)
        data = self.waiter_until_list(self.LOCATOR_FIRST_TASK_IMG_SEARCH)
        return data