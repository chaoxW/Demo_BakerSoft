from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        # validate the signup link is visible
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        # validate the login page title is correct
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    # the signup form is visible after click the register button
    def test_signup_form_visible(self):
        self.loginPage = LoginPage(self.driver)
        # click the signup link
        self.loginPage.click_signup_link()
        # validate the signup form is visible
        form = self.loginPage.is_signup_form_title_exist()
        assert form

    # the signup form is visible after click the register button
    def test_signup_form_errors(self):
        self.loginPage = LoginPage(self.driver)
        # click the signup link
        self.loginPage.click_signup_link()
        # click register button
        self.loginPage.click_register_button()
        # validate the error messages from the form inputs
        self.loginPage.get_firstname_input_error()
        self.loginPage.get_lastname_input_error()
        self.loginPage.get_address_input_error()
        self.loginPage.get_zipcode_input_error()
        self.loginPage.get_ssn_input_error()
        self.loginPage.get_username_input_error()
        self.loginPage.get_password_input_error()

    # login with invalid username and password check the error message
    def test_login_error(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_with_error(TestData.USER_NAME, TestData.PASSWORD)
