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
    LOCATOR_FIRST_TASK_LINK_SEARCH_ANOTHER = (
        By.CLASS_NAME,
        'tensor_ru-link tensor_ru-Index__link')
    LOCATOR_INVISIBILITY_ELEMENT = (
        By.XPATH,
        "//div[@class='tensor_ru-messages-container']"
    )
    LOCATOR_INVISIBILITY_ELEMENT_CLOSE = (
        By.XPATH,
        "//div[@class = 'tensor_ru-CookieAgreement__close icon-Close ws-flex-shrink-0 ws-flexbox ws-align-items-center']"
    )
    
    def FindFirstPhrase(self):
        self.get("https://tensor.ru/")
        data = self.waiter_until(self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)
        # self.find(self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)
        return data
    
    # def TextLinkOpen(self):
    #     self.get("https://tensor.ru/")
    #     # link = self.find(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
    #     link = self.waiter_until(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
    #     # another_link = "https://oleg.ru/"
    #     another_link = link.get_attribute('href')
    #     # new = self.get(another_link)
    #     link.click()
    #     # new = self.get("https://oleg.ru/")
    #     url = self.url()
    #     return [another_link, url]
    def TextLinkOpen(self):
        self.get("https://tensor.ru/")
        time.sleep(7)
        # link = self.find(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
        link = self.waiter_until(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
        # link = self.waiter_clicable(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
        # link = self.waiter_until_list(self.LOCATOR_FIRST_TASK_LINK_SEARCH_ANOTHER)
        another_link = link.get_attribute('href')
        # self.invisibility_element(self.LOCATOR_INVISIBILITY_ELEMENT)
        action = ActionChains(self.driver)
        action.click(self.waiter_until(self.LOCATOR_INVISIBILITY_ELEMENT_CLOSE)).perform()
        action.click(link).perform()
        # self.driver.execute_script("arguments[0].click();",link)
        # time.sleep(20)
        # self.waiter_new_url()
        # another_link = "https://oleg.ru/"
        # new = self.get(another_link)
        # new = self.get("https://oleg.ru/")
        url = self.url()
        return [another_link, url]