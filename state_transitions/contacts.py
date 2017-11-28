from pages.add_a_contact import AddPersonPage
from pages.contact import ContactPage
from pages.contacts import ContactsPage
from yeager import state_transition, add_transition_to_blacklist, remove_transition_from_blacklist
from data.generators import get_lastname, get_firstname

@state_transition("contacts-page", "add-contact-page", weight=5)
def add_someone(driver):
    contacts = ContactsPage(driver)
    contacts.click_add_person()
    add_transition_to_blacklist(okay_add) #cant proceed until they have a first name

@state_transition("add-contact-page", "contacts-page")
def cancel_add(driver):
    add = AddPersonPage(driver)
    add.click_cancel_button()

@state_transition("add-contact-page", "add-contact-page", weight=5)
def add_firstname(driver):
    add = AddPersonPage(driver)
    add.set_first_name(get_firstname())
    remove_transition_from_blacklist(okay_add) #now we can proceed

@state_transition("add-contact-page", "add-contact-page")
def add_lastname(driver):
    add = AddPersonPage(driver)
    add.set_last_name(get_lastname())

@state_transition("add-contact-page", "contact-page", weight=5)
def okay_add(driver):
    add = AddPersonPage(driver)
    add.click_add_button()

@state_transition("contact-page", "edit-contact-page")
def edit_contact(driver):
    contact = ContactPage(driver)
    contact.click_edit_contact()
