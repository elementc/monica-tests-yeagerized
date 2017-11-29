from selenium import webdriver
from yeager import walk

# parse the transtitions...
import state_transitions.headerpage
import state_transitions.login

# this script synthesizes the bug when you click through creating a contact without typing a name
# it must reimplement state_transitions.contacts in an inferior way.

from pages.add_a_contact import AddPersonPage
from pages.contact import ContactPage
from yeager import state_transition

@state_transition("contacts-page", "add-contact-page", weight=5)
def add_someone(driver):
    contacts = ContactsPage(driver)
    contacts.click_add_person()

@state_transition("add-contact-page", "contact-page")
def okay_add(driver):
    add = AddPersonPage(driver)
    add.click_add_button()

walk(driver=webdriver.Chrome())
