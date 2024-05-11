from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
import time

class SecondTaskPage(BasePage):

    LOCATOR_SECOND_TASK_REGION = (
        By.XPATH,
        "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']//preceding-sibling::span")
    LOCATOR_SECOND_TASK_LIST_OF_ORGS = (
        By.XPATH,
        "//div[@class='controls-ListView__itemV-relative controls-ListView__itemV controls-ListView__item_default js-controls-ListView__editingTarget  controls-ListView__itemV_cursor-pointer  controls-ListView__item_showActions js-controls-ListView__measurableContainer controls-ListView__item__unmarked_default controls-ListView__item_highlightOnHover controls-hover-background-default controls-Tree__item']")
    LOCATOR_CLICK_ACTION = (
        By.XPATH,
        "//span[@title='Камчатский край']")
    LOCATOR_NEW_PAGE_TITLE = (
        By.XPATH,
        # "//title[@class='state-1']"
        "//title[@sid='h-6']"
    )
    def RegionCheck(self):
        self.get("https://sbis.ru/contacts")
        region = self.waiter_until(self.LOCATOR_SECOND_TASK_REGION).text
        list_of_orgs = self.waiter_until_list(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS)
        return region, list_of_orgs
    
    def RegionSwitchCheck(self):
        self.get("https://sbis.ru/contacts")
        region = self.waiter_until(self.LOCATOR_SECOND_TASK_REGION).text
        print(self.waiter_until(self.LOCATOR_NEW_PAGE_TITLE).text)
        print(region)
        list_of_orgs = self.waiter_until_list(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS)[0].get_attribute("textContent")
        pre_url = self.url()
        self.action_click(self.waiter_until(self.LOCATOR_SECOND_TASK_REGION))
        self.action_click(self.waiter_until(self.LOCATOR_CLICK_ACTION))
        self.waiter_new_url(pre_url)
        url = self.url()
        title_of_new_page = self.waiter_until(self.LOCATOR_NEW_PAGE_TITLE).get_attribute("textContent")
        print(title_of_new_page)
        new_region = str(self.waiter_until(self.LOCATOR_SECOND_TASK_REGION).text)
        new_list_of_orgs = self.waiter_until_list(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS)[0].get_attribute("textContent")
        return region, list_of_orgs, url, title_of_new_page, new_region, new_list_of_orgs

