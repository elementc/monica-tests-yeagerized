from .page_base import PageBase
from .dashboard import DashboardPage
import os
from selenium.webdriver.common.by import By

class LoginPage(PageBase):
    def initial_status(self):
        assert 'MONICA_USERNAME' in os.environ, "Must set a login username as environment var MONICA_USERNAME."
        assert 'MONICA_PASSWORD' in os.environ, "Must set a login password as environment var MONICA_PASSWORD."
        self.username = os.environ['MONICA_USERNAME']
        self.password = os.environ['MONICA_PASSWORD']

    email_selector = (By.ID, "email")
    password_selector = (By.ID, "password")
    login_btn_selector = (By.CSS_SELECTOR, "button.btn.btn-primary:nth-of-type(1)")
    def log_in_correctly(self) -> DashboardPage:
        email_field = self.driver.find_element(*self.email_selector)
        password_field = self.driver.find_element(*self.password_selector)
        login_button = self.driver.find_element(*self.login_btn_selector)
        email_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()
        return DashboardPage(self.driver)
