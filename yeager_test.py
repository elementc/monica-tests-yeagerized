from selenium import webdriver
from pages.login import LoginPage
from pages.dashboard import DashboardPage
from pages.header_page import HeaderPage
from pages.contacts import ContactsPage
from pages.add_a_contact import AddPersonPage
from pages.contact import ContactPage
from pages.edit_contact import EditContactPage
from yeager import walk
from yeager.annotations import state_transition
driver = None

@state_transition(None, "login-page")
def open(driver):
    driver.get("https://monica-doran.herokuapp.com/")

@state_transition("login-page", "dashboard-page")
def log_in(driver):
    login = LoginPage(driver)
    login.log_in_correctly()

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

@state_transition("contacts-page", "add-contact-page")
def add_someone(driver):
    contacts = ContactsPage(driver)
    contacts.click_add_person()

@state_transition("add-contact-page", "contacts-page")
def cancel_add(driver):
    add = AddPersonPage(driver)
    add.click_cancel_button()

@state_transition("add-contact-page", "contact-page")
def okay_add(driver):
    add = AddPersonPage(driver)
    add.click_add_button()

@state_transition("contact-page", "edit-contact-page")
def edit_contact(driver):
    contact = ContactPage(driver)
    contact.click_edit_contact()

walk(50, driver=webdriver.Chrome())
