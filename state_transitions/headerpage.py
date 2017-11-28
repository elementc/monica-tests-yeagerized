from pages.header_page import HeaderPage
from yeager import state_transition

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "login-page")
def log_out(driver):
    header = HeaderPage(driver)
    header.log_out()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "dashboard-page")
def dashboard_page(driver):
    header = HeaderPage(driver)
    header.go_dashboard()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "contacts-page")
def contacts_page(driver):
    header = HeaderPage(driver)
    header.go_contacts()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "journal-page")
def journal_page(driver):
    header = HeaderPage(driver)
    header.go_journal()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "settings-page")
def settings_page(driver):
    header = HeaderPage(driver)
    header.go_settings()
