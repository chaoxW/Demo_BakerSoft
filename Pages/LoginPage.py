from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "username")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH,
                    "//body/div[@id='mainPanel']/div[@id='bodyPanel']/div[@id='leftPanel']/div[@id='loginPanel']/form[1]/div[3]/input[1]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Log Out')]")
    SIGNUP_LINK = (By.LINK_TEXT, "Register")
    REGISTER_BUTTON = (By.XPATH, "//tbody/tr[13]/td[2]/input[1]")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'The username and password could not be verified.')]")
    LOGIN_PANEL = (By.ID, "loginPanel")
    SIGNUP_FORM = (By.ID, "customerForm")
    SIGNUP_TITLE = (By.XPATH, "//h1[contains(text(),'Signing up is easy!')]")
    FIRSTNAME_INPUT_ERROR = (By.ID, "customer.firstName.errors")
    LASTNAME_INPUT_ERROR = (By.ID, "customer.lastName.errors")
    ADDRESS_INPUT_ERROR = (By.ID, "customer.address.street.errors")
    ZIPCODE_INPUT_ERROR = (By.ID, "customer.address.zipCode.errors")
    SSN_INPUT_ERROR = (By.ID, "customer.ssn.errors")
    USERNAME_INPUT_ERROR = (By.ID, "customer.username.errors")
    PASSWORD_INPUT_ERROR = (By.ID, "customer.password.errors")

    # constructor of the page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def get_firstname_input_error(self):
        return self.is_visible(self.FIRSTNAME_INPUT_ERROR)

    def get_lastname_input_error(self):
        return self.is_visible(self.LASTNAME_INPUT_ERROR)

    def get_address_input_error(self):
        return self.is_visible(self.ADDRESS_INPUT_ERROR)

    def get_zipcode_input_error(self):
        return self.is_visible(self.ZIPCODE_INPUT_ERROR)

    def get_ssn_input_error(self):
        return self.is_visible(self.SSN_INPUT_ERROR)

    def get_username_input_error(self):
        return self.is_visible(self.USERNAME_INPUT_ERROR)

    def get_password_input_error(self):
        return self.is_visible(self.PASSWORD_INPUT_ERROR)

    def is_signup_form_title_exist(self):
        return self.is_visible(self.SIGNUP_TITLE)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def click_signup_link(self):
        return self.do_click(self.SIGNUP_LINK)

    def click_register_button(self):
        return self.do_click(self.REGISTER_BUTTON)

    def do_login_with_error(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        self.is_visible(self.LOGIN_ERROR)
