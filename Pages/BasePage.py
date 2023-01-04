from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return el.text

    def is_visible(self, by_locator):
        el = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(el)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def get_element_by_id(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
