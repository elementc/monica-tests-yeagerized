from selenium import webdriver
from pages.login import LoginPage
from pages.dashboard import DashboardPage
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

@state_transition("dashboard-page", "login-page")
def log_out():
    dashboard = DashboardPage(driver)
    dashboard.log_out()

@state_transition("login-page", None)
def close():
    global driver
    driver.close()

walk(10)
