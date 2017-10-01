from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class DashboardPage(HeaderPage):
    dashboard_selector = (By.CSS_SELECTOR, "div.dashboard")

    def initial_status(self):
        # make sure there is a dashboard div visible...
        self.driver.find_element(*self.dashboard_selector)
        HeaderPage.initial_status(self)
