
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class AnaplanMainPage(BasePage):


    USER_NAME_ID = (By.XPATH,"//li[@id='user-menu']//child::em")


    def __init__(self, driver):
        self.driver = driver


    def get_user_name(self):
        return self.get_element_text(self.USER_NAME_ID)