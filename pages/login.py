from .page_base import PageBase
from .dashboard import DashboardPage
import os

class LoginPage(PageBase):
    def initial_status(self):
        assert 'MONICA_USERNAME' in os.environ, "Must set a login username as environment var MONICA_USERNAME."
        assert 'MONICA_PASSWORD' in os.environ, "Must set a login password as environment var MONICA_PASSWORD."
        self.username = os.environ['MONICA_USERNAME']
        self.password = os.environ['MONICA_PASSWORD']

    def log_in_correctly(self) -> DashboardPage:
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        login_button = self.driver.find_element_by_css_selector("button.btn.btn-primary")
        email_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()
        self.driver.find_element_by_css_selector("div.dashboard")
        return DashboardPage(self.driver)
