from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class ContactsPage(HeaderPage):
    add_person_button_sel = (By.LINK_TEXT, "Add someone")

    def click_add_person(self)->'AddPersonPage':
        add_person = self.driver.find_element(*self.add_person_button_sel)
        add_person.click()
        from .add_a_contact import AddPersonPage
        return AddPersonPage(self.driver)

    def open_existing_person(self)-> 'ContactPage':
        pass
        #TODO: pick a random person that's here
