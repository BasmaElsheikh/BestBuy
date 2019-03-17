import unittest
from pages.login_page import LoginPage
from pages.top_panel_page import TopPanelPage
from pages.popup_page import PopupPage
import pytest

@pytest.mark.usefixtures('one_time_setup')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse = True)
    def class_setup(self):
        self.top_panel = TopPanelPage(self.driver)
        self.popup = PopupPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        if self.popup.signup_popup_displayed():
            self.popup.click_signup_close_button()
        self.top_panel.click_signin_link()

    def test_invalidLogin(self):
        print('starting invalid login test')
        self.login_page.login()
        if self.login_page.error_message_displayed():                                                                   #verify error message is generated
             print("error message generated")
        else:
            print("ERROR: error message not generated")

    def test_validLogin(self):
        print('starting valid login test')
        self.login_page.login('basma.elsheikh@gmail.com', '4BestBuy')
        if self.top_panel.signout_link_displayed():                                                                     #verify login is  successful
             print("login successful")
        else:
            print("ERROR: login not successful")

