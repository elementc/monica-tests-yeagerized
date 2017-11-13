from .header_page import HeaderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class EditContactPage(HeaderPage):
    delete_btn_sel = (By.LINK_TEXT, "click here")
    first_name_field_sel = (By.NAME, "first_name")
    last_name_field_sel = (By.NAME, "last_name")
    gender_none_radio_sel = (By.ID, "none")
    gender_male_radio_sel = (By.ID, "male")
    gender_female_radio_sel = (By.ID, "female")
    cancel_button_sel = (By.LINK_TEXT, "Cancel")
    save_button_sel = (By.CSS_SELECTOR, "form button.btn.btn-primary")

    def delete_this_contact(self):
        delete_btn = self.driver.find_element(*self.delete_btn_sel)
        delete_btn.click()
        Alert(self.driver).accept()
        from .contacts import ContactsPage
        return ContactsPage(self.driver)

    def set_gender_male(self):
        pass

    def set_gender_male(self):
        pass

    def set_gender_female(self):
        pass

    def set_first_name(self, fname):
        pass

    def set_last_name(self, lname):
        pass

    def set_street(self, sname):
        pass

    def set_city(self, cname):
        pass

    def set_province(self, pname):
        pass

    def set_postcode(self, pcode):
        pass

    def set_country(self, cname):
        pass

    def set_email_address(self, ename):
        pass

    def set_phone(self, pname):
        pass

    def set_facebook(self, fname):
        pass

    def set_twitter(self, tname):
        pass

    def set_dont_know_age(self):
        pass

    def set_probable_age(self, p_age):
        pass

    def set_birthdate(self, bdate):
        pass

    def set_deceased_status(self, isdeceased):
        pass

    def set_is_deceased(self):
        pass

    def set_is_not_deceased(self):
        pass

    def set_dont_know_deceased_date(self):
        pass

    def set_know_deceased_date_status(self, know_deceased_date):
        pass

    def set_know_deceased_date(self):
        pass

    def set_deceased_date(self, date):
        pass

    def set_add_deceased_reminder_status(self, add_reminder):
        pass

    def set_add_deceased_reminder(self):
        pass

    def set_dont_add_deceased_reminder(self):
        pass

    def click_cancel_button(self):
        pass

    def click__save_button(self):
        pass
