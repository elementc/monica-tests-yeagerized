from selenium import webdriver
from pages.login import LoginPage
from pages.dashboard import DashboardPage
from pages.header_page import HeaderPage
from yeager import walk
from yeager.annotations import state_transition
driver = None

@state_transition(None, "login-page")
def open():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://app.monicahq.com/")

@state_transition("login-page", "dashboard-page")
def log_in():
    login = LoginPage(driver)
    login.log_in_correctly()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "login-page")
def log_out():
    header = HeaderPage(driver)
    header.log_out()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "dashboard-page")
def dashboard_page():
    header = HeaderPage(driver)
    header.go_dashboard()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "contacts-page")
def contacts_page():
    header = HeaderPage(driver)
    header.go_contacts()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "journal-page")
def journal_page():
    header = HeaderPage(driver)
    header.go_journal()

@state_transition(["dashboard-page", "contacts-page", "journal-page", "settings-page"], "settings-page")
def settings_page():
    header = HeaderPage(driver)
    header.go_settings()

# @state_transition("login-page", None)
def close():
    global driver
    driver.close()

walk(50)
