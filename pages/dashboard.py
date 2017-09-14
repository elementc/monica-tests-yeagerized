from .page_base import PageBase
from selenium.webdriver.common.by import By

class DashboardPage(PageBase):
    dashboard_selector = (By.CSS_SELECTOR, "div.dashboard")
    def initial_status(self):
        # make sure there is a dashboard div visible...
        self.driver.find_element(*self.dashboard_selector)
