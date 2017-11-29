from pages.header_page import HeaderPage
from yeager import state_transition
header_page_startstates = ["dashboard-page", "contacts-page", "journal-page", "settings-page", "contact-page"]

@state_transition(header_page_startstates, "login-page")
def log_out(driver):
    header = HeaderPage(driver)
    header.log_out()

@state_transition(header_page_startstates, "dashboard-page")
def dashboard_page(driver):
    header = HeaderPage(driver)
    header.go_dashboard()

@state_transition(header_page_startstates, "contacts-page")
def contacts_page(driver):
    header = HeaderPage(driver)
    header.go_contacts()

@state_transition(header_page_startstates, "journal-page")
def journal_page(driver):
    header = HeaderPage(driver)
    header.go_journal()

@state_transition(header_page_startstates, "settings-page")
def settings_page(driver):
    header = HeaderPage(driver)
    header.go_settings()
