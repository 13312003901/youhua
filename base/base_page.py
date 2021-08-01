import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from log import log
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self,url=None):
        if url is None:
            self.driver.get(self.url)
        else :
            self.driver.get(url)

    def by_id(self,id_):
        self.driver.find_element_by_id(id_)
        return

    #def find_element(self, *loc):
    #    return self.driver.find_element(*loc)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())

            return self.driver.find_element(*loc)
        except Exception as e:
            print("未找到%s" % (self, loc))

    def slepp(self,sec):
        time.sleep(sec)
