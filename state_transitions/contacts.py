from pages.add_a_contact import AddPersonPage
from pages.contact import ContactPage
from pages.contacts import ContactsPage
from yeager import state_transition

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
