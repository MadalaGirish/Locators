import pytest
from driver import driver
from Pages.Login_page import login_page
from Test.Test_base import Basetest
from config.config import Testdata


class Test_login(Basetest):
    """Validating Login Credentials"""
    """Click on sign-up """

    def test_login(self):
        self.loginpage = login_page(self.driver)
        self.loginpage.Login_in(Testdata.Candidate, Testdata.Password)

    """Verify title"""

    def test_login_title(self):
        self.loginpage = login_page(self.driver)
        title = self.loginpage.get_title(Testdata.LoginPageTitle)
        assert title == Testdata.LoginPageTitle
        print(Testdata.LoginPageTitle)
        driver.title()
        print(title)
