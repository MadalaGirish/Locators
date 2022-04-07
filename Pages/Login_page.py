from selenium.webdriver.common.by import By
from Pages.Basepage import Basepage
from Pages.Canditate_page import Homepage
from config.config import Testdata


class login_page(Basepage):
    """"locators"""
    Email = (By.ID, "email")
    Password = (By.ID, "password")
    Sign_up = (By.XPATH, "//span[@class='MuiButton-label']")

    """constructor"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.Base_Url)
        """Page actions"""

    """title"""

    def get_login_title(self, title):
        return self.get_title(title)

    """Sig_up_link"""

    def sign_up_link(self):
        return self.is_visible(self.Sign_up)

    """Take to Login page """

    def Login_in(self, username, password):
        self.do_send_keys(self.Email, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.Sign_up)
        return Homepage(self.driver)
