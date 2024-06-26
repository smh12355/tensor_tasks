from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import os

class FirstTaskPage(BasePage):
    LOCATOR_BUTTON_CONTACTS = (
        By.XPATH,
        "//a[@class='sbisru-Header__menu-link sbisru-Header__menu-link--hover' and text()='Контакты']"
    )
    LOCATOR_PICTURE_TENSOR_CLICK = (
        By.XPATH,
        "//a[@class='sbisru-Contacts__logo-tensor mb-12']"
    )
    LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH = (
        By.XPATH,
        "//p[@class='tensor_ru-Index__card-title tensor_ru-pb-16' and text()='Сила в людях']"
    )
    LOCATOR_FIRST_TASK_LINK_SEARCH = (
        By.XPATH, 
        "//a[@class='tensor_ru-link tensor_ru-Index__link' and @href='/about']"
    )
    LOCATOR_INVISIBILITY_ELEMENT_CLOSE = (
        By.XPATH,
        "//div[@class = 'tensor_ru-CookieAgreement__close icon-Close ws-flex-shrink-0 ws-flexbox ws-align-items-center']"
    )   
    LOCATOR_FIRST_TASK_IMG_SEARCH = (
        By.XPATH, 
        "//div[@class='tensor_ru-About__block3-image-filter']//preceding-sibling::img"
    )
    LOCATOR_BUTTON_ABOUT = (
        By.XPATH,
        "//a[@class='tensor_ru-Header__menu-link' and text()='О компании']"
    )
    LOCATOR_TITLE = (
        By.XPATH,
        "//title[@class='state-1']"
    )
    LOCATOR_LINK_TO_DOWNLOADER = (
        By.XPATH,
        "//a[@class='sbisru-Footer__link' and text()='Скачать локальные версии']"
    )
    LOCATOR_PLAGIN_BUTTON = (
        By.XPATH,
        "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']"
    )
    LOCATOR_DOWNLOAD = (
        By.XPATH,
        "//a[@class='sbis_ru-DownloadNew-loadLink__link js-link' and @href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']"
    )
    LOCATOR_INVISIBILITY_ELEMENT_CLOSE_ANOTHER = (
        By.XPATH,
        "//div[@class='sbis_ru-CookieAgreement__close']"
    )
    URL = "https://sbis.ru/"
    def FindFirstPhrase(self):
        self.get(self.URL)
        pre_url = self.url()
        self.action_click(self.waiter_until(self.LOCATOR_BUTTON_CONTACTS))
        self.waiter_new_url(pre_url)
        self.action_click(self.waiter_until(self.LOCATOR_PICTURE_TENSOR_CLICK))
        self.switch_betwen_tables(1)
        data = self.waiter_until(self.LOCATOR_FIRST_TASK_HUM_STRENGHT_SEARCH)
        return data
    
    def TextLinkOpen(self):
        self.get(self.URL)
        pre_url = self.url()
        self.action_click(self.waiter_until(self.LOCATOR_BUTTON_CONTACTS))
        self.waiter_new_url(pre_url)
        self.action_click(self.waiter_until(self.LOCATOR_PICTURE_TENSOR_CLICK))
        self.wait_new_tab_open(2)
        _ = self.waiter_until(self.LOCATOR_TITLE)
        self.switch_betwen_tables(1)
        link = self.waiter_until(self.LOCATOR_FIRST_TASK_LINK_SEARCH)
        another_link = link.get_attribute('href')
        self.action_click(self.waiter_until(self.LOCATOR_INVISIBILITY_ELEMENT_CLOSE))
        pre_url = self.url()
        time.sleep(2)
        self.action_click(link)
        self.waiter_new_url(pre_url)
        url = self.url()
        return [another_link, url]
    
    def SizeOfPictures(self):
        self.get(self.URL)
        pre_url = self.url()
        self.action_click(self.waiter_until(self.LOCATOR_BUTTON_CONTACTS))
        self.waiter_new_url(pre_url)
        self.action_click(self.waiter_until(self.LOCATOR_PICTURE_TENSOR_CLICK))
        self.switch_betwen_tables(1)
        pre_url = self.url()
        self.action_click(self.waiter_until(self.LOCATOR_BUTTON_ABOUT))
        self.waiter_new_url(pre_url)
        data = self.waiter_until_list(self.LOCATOR_FIRST_TASK_IMG_SEARCH)
        return data
    
    def DownloadCheck(self):
        self.get(self.URL)
        pre_url = self.url()
        self.action_click(self.waiter_until(self.LOCATOR_INVISIBILITY_ELEMENT_CLOSE_ANOTHER))
        time.sleep(2)
        self.action_click(self.waiter_until(self.LOCATOR_LINK_TO_DOWNLOADER))
        self.waiter_new_url(pre_url)
        self.action_click(self.waiter_until(self.LOCATOR_PLAGIN_BUTTON))
        size_from_webpage = self.waiter_until(self.LOCATOR_DOWNLOAD).get_attribute("textContent")
        pre_size = re.search(r'\d+\.\d+', size_from_webpage).group()
        round_number = len(pre_size.split('.')[1])
        self.action_click(self.waiter_until(self.LOCATOR_DOWNLOAD))
        path = os.path.join(os.path.dirname(__file__),"..","tests","sbisplugin-setup-web.exe")
        while (os.path.isfile(path) is False):
            time.sleep(1)
        size = round(os.path.getsize(path) / (1024 ** 2), round_number)
        os.remove(path)
        return size, pre_size