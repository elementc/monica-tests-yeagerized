from .page_base import PageBase
from selenium.webdriver.common.by import By

class DashboardPage(PageBase):
    dashboard_selector = (By.CSS_SELECTOR, "div.dashboard")
    logout_selector = (By.LINK_TEXT, "Logout")
    def initial_status(self):
        # make sure there is a dashboard div visible...
        self.driver.find_element(*self.dashboard_selector)

    def log_out(self):
        btn = self.driver.find_element(*self.logout_selector)
        btn.click()
        from .login import LoginPage
        return LoginPage(self.driver)
