import time

import pytest
from Pages.AnaplanLoginPage import AnaplanLoginPage
from Pages.AnaplanMainPage import AnaplanMainPage
from Tests.BaseTest import BaseTest


class TestPage(BaseTest):

    COMPANY_NAME = "Test24"
    EMAIL_ADDRESS = "mintigo20@gmail.com"
    PASSWORD = "Anaplan21"

    @pytest.fixture(autouse=True)
    def setup_module(self):
        self.anaplan_login_page = AnaplanLoginPage(self.driver)


    def test_correct_inputs_login(self):
        #setting text fields
        self.anaplan_login_page.set_company_name(self.COMPANY_NAME)
        self.anaplan_login_page.set_email(self.EMAIL_ADDRESS)
        self.anaplan_login_page.set_password(self.PASSWORD)
        #perfom click
        if not self.anaplan_login_page.click_signin():
           assert False

        else:
            self.anaplan_main_page = AnaplanMainPage(self.anaplan_login_page.driver)
            #check if the COMPANY_NAME in main page
            if self.anaplan_main_page.get_user_name() != self.COMPANY_NAME:
                assert False



    def test_wrong_inputs_login(self):

        self.anaplan_login_page.set_company_name("123")
        self.anaplan_login_page.set_email("123")
        self.anaplan_login_page.set_password("123")
        # perfom click
        if not self.anaplan_login_page.click_signin():
            assert False

