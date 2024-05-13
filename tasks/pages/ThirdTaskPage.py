from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
import os
import time
import re

class ThirdTaskPage(BasePage):
    LOCATOR_LINK_TO_DOWNLOADER = (
        By.XPATH,
        "//a[@class='sbisru-Footer__link' and text()='Скачать локальные версии']"
    )
    LOCATOR_PLAGIN_BUTTON = (
        By.XPATH,
        "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']"
    )
    LOCATOR_INVISIBILITY_ELEMENT_CLOSE = (
        By.XPATH,
        "//div[@class='sbis_ru-CookieAgreement__close']"
    )
    LOCATOR_DOWNLOAD = (
        By.XPATH,
        "//a[@class='sbis_ru-DownloadNew-loadLink__link js-link' and @href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']"
    )   

    def DownloadCheck(self):
        self.get("https://sbis.ru/")
        pre_url = self.url()
        self.action_click(self.waiter_until(self.LOCATOR_INVISIBILITY_ELEMENT_CLOSE))
        time.sleep(1)
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
        
