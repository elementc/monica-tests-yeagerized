from pages.login import LoginPage
from yeager import state_transition

@state_transition(None, "login-page")
def open(driver):
    driver.get("https://monica-doran.herokuapp.com/")

@state_transition("login-page", "dashboard-page")
def log_in(driver):
    login = LoginPage(driver)
    login.log_in_correctly()
