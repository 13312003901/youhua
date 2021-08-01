from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage

class LoginPage(BasePage):
    loginid_loc = (By.ID,"loginId")
    password_loc = (By.ID,"password")
    login_button = (By.XPATH,'//button')

    url = "http://stage.raiborn:8006"


    def loginid_input(self,loginid_key):
        self.find_element(*self.loginid_loc).send_keys(loginid_key)

    def password_input(self,password_key):
        self.find_element(*self.password_loc).send_keys(password_key)

    def login_click(self):
        self.find_element(*self.login_button).click()

    def login(self):
        sleep(3)
        self.loginid_input("zmh")
        self.password_input("zmh")
        sleep(2)
        self.login_click()
        sleep(5)


