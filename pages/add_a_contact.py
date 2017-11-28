from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class AddPersonPage(HeaderPage):
    first_name_field_sel = (By.NAME, "first_name")
    last_name_field_sel = (By.NAME, "last_name")
    gender_none_radio_sel = (By.ID, "none")
    gender_male_radio_sel = (By.ID, "male")
    gender_female_radio_sel = (By.ID, "female")
    cancel_button_sel = (By.LINK_TEXT, "Cancel")
    add_button_sel = (By.CSS_SELECTOR, "form button.btn.btn-primary")

    def set_first_name(self, first_name):
        field = self.driver.find_element(*self.first_name_field_sel)
        field.clear()
        field.send_keys(first_name)

    def set_last_name(self, last_name):
        field = self.driver.find_element(*self.last_name_field_sel)
        field.clear()
        field.send_keys(last_name)

    def set_gender_none(self):
        radio = self.driver.find_element(*self.gender_none_radio_sel)
        radio.click()

    def set_gender_male(self):
        radio = self.driver.find_element(*self.gender_male_radio_sel)
        radio.click()

    def set_gender_female(self):
        radio = self.driver.find_element(*self.gender_female_radio_sel)
        radio.click()

    def click_cancel_button(self) -> 'ContactsPage':
        btn = self.driver.find_element(*self.cancel_button_sel)
        btn.click()
        from .contacts import ContactsPage
        return ContactsPage(self.driver)

    def click_add_button(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.add_button_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)
