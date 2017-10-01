from .page_base import PageBase
from selenium.webdriver.common.by import By

class HeaderPage(PageBase):
    header_selector = (By.TAG_NAME, "header")
    dashboard_link_selector = (By.LINK_TEXT, "Dashboard")
    contacts_selector = (By.LINK_TEXT, "Contacts")
    journal_selector = (By.LINK_TEXT, "Journal")
    settings_selector = (By.LINK_TEXT, "Settings")
    logout_selector = (By.LINK_TEXT, "Logout")

    def initial_status(self):
        #verify header is visible
        self.driver.find_element(*self.header_selector)
        PageBase.initial_status(self)

    def log_out(self) -> 'LoginPage':
        btn = self.driver.find_element(*self.logout_selector)
        btn.click()
        from .login import LoginPage
        return LoginPage(self.driver)

    def go_dashboard(self) -> 'DashboardPage':
        btn = self.driver.find_element(*self.dashboard_link_selector)
        btn.click()
        from .dashboard import DashboardPage
        return DashboardPage(self.driver)

    def go_contacts(self) -> 'ContactsPage':
        btn = self.driver.find_element(*self.contacts_selector)
        btn.click()
        from .contacts import ContactsPage
        return ContactsPage(self.driver)

    def go_journal(self) -> 'JournalPage':
        btn = self.driver.find_element(*self.journal_selector)
        btn.click()
        from .journal import JournalPage
        return JournalPage(self.driver)

    def go_settings(self) -> 'SettingsPage':
        btn = self.driver.find_element(*self.settings_selector)
        btn.click()
        from .settings import SettingsPage
        return SettingsPage(self.driver)
