from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class AnaplanLoginPage(BasePage):

    SIGN_IN_BUTTON_ID = (By.XPATH,"//button[.='Sign in']")

    CUSTOMER_NAME_ID = (By.ID,"customer_name")
    EMAIL_ID =(By.ID, "user_email")
    PASSWORD_ID = (By.ID,"pass")


    def __init__(self, driver):
        self.driver = driver



    def set_company_name(self,name):
        self.send_keys(self.CUSTOMER_NAME_ID,name)

    def set_email(self,mail):
        self.send_keys(self.EMAIL_ID,mail)

    def set_password(self,password):
        self.send_keys(self.PASSWORD_ID,password)

    def click_signin(self):
         return self.perform_click(self.SIGN_IN_BUTTON_ID)
