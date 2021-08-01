import random

from selenium.webdriver.common.by import By

from base.base_page import BasePage

class NationPage(BasePage):

    insert_nation = (By.XPATH,'//*[@id="root"]/div/section/section/main/div[2]/div/div[1]/div[1]/button')
    nation_daima = (By.ID,'canvas1607325178847_tabgroup_522_tab_2_sectionrow_1628_sectioncol_1730_textbox_2538')
    nation_chinese = (By.ID,'canvas1607325178847_tabgroup_522_tab_2_sectionrow_1628_sectioncol_1831_textbox_2740')
    nation_english = (By.ID, 'canvas1607325178847_tabgroup_522_tab_2_sectionrow_1628_sectioncol_1932_textbox_2639')
    save_button = (By.XPATH,'//*[@id="root"]/div/section/section/main/div[2]/div/div[1]/div/button[3]')

    #进入国别菜单
    def enter_nation(self):
       self.driver.find_elements_by_xpath(
           '//*[@id="root"]/div/section/section/header/div/div/div[1]/div[2]/div/div/div[7]/span')[0].click()
    #点击新增按钮
    def insert_click(self):
        self.find_element(*self.insert_nation).click()
    #输入国别代码
    def daima_input(self):
        self.find_element(*self.nation_daima).send_keys(random.sample("2468ffdf",5))
    #输入中文名称
    def chinese_input(self):
        self.find_element(*self.nation_chinese).send_keys(random.sample("2468ffdf",5))
    #输入英文名称
    def english_input(self):
        self.find_element(*self.nation_english).send_keys(random.sample("2468ffdf",5))

    #点击保存按钮
    def save_click(self):
        self.find_element(*self.save_button).click()