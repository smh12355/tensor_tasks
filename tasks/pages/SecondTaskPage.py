from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
import pytest

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
        "//title[@class='state-1']"
    )
    def RegionCheck(self):
        self.get("https://sbis.ru/contacts")
        # region = self.find(self.LOCATOR_SECOND_TASK_REGION).text
        # list_of_orgs = self.find_list(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS)
        # region = self.waiter.until(EC.presence_of_element_located(self.LOCATOR_SECOND_TASK_REGION)).text
        # list_of_orgs = self.waiter.until(EC.presence_of_all_elements_located(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS))
        region = self.waiter_until(self.LOCATOR_SECOND_TASK_REGION).text
        list_of_orgs = self.waiter_until_list(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS)
        return region, list_of_orgs
    
    def RegionSwitchCheck(self):
        self.get("https://sbis.ru/contacts")
        waiter = self.wait()
        pytest.set_trace() 
        # region = self.find(self.LOCATOR_SECOND_TASK_REGION).text
        # list_of_orgs = self.find_list(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS)
        region = waiter.until(EC.presence_of_element_located(self.LOCATOR_SECOND_TASK_REGION)).text
        list_of_orgs = waiter.until(EC.presence_of_all_elements_located(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS))
        # self.find(self.LOCATOR_SECOND_TASK_REGION).click()
        # self.find(self.LOCATOR_CLICK_ACTION).click()
        waiter.until(EC.presence_of_element_located(self.LOCATOR_SECOND_TASK_REGION)).click()
        waiter.until(EC.presence_of_element_located(self.LOCATOR_CLICK_ACTION)).click()
        url = self.url()
        print(url)
        title_of_new_page = self.find("//title[@class='state-1']").text
        print(title_of_new_page)
        new_region = self.find(self.LOCATOR_SECOND_TASK_REGION).text
        print(new_region)
        new_list_of_orgs = self.find_list(self.LOCATOR_SECOND_TASK_LIST_OF_ORGS)
        print(new_list_of_orgs)
        return region, list_of_orgs, url, title_of_new_page, new_region, new_list_of_orgs

