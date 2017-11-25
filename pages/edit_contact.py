from .header_page import HeaderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class OptionNotFoundException(Exception):
    pass

class EditContactPage(HeaderPage):
    delete_btn_sel = (By.LINK_TEXT, "click here")
    first_name_field_sel = (By.NAME, "firstname")
    last_name_field_sel = (By.NAME, "lastname")
    gender_none_radio_sel = (By.ID, "genderNone")
    gender_male_radio_sel = (By.ID, "genderMale")
    gender_female_radio_sel = (By.ID, "genderFemale")
    cancel_button_sel = (By.LINK_TEXT, "Cancel")
    save_button_sel = (By.CSS_SELECTOR, "form button.btn.btn-primary")
    street_field_sel = (By.ID, "street")
    city_field_sel = (By.ID, "city")
    province_field_sel = (By.ID, "province")
    postcode_field_sel = (By.ID, "postalcode")
    country_selector_sel = (By.NAME, "country")
    email_field_sel = (By.ID, "email")
    phone_field_sel = (By.ID, "phone")
    facebook_field_sel = (By.ID, "facebook")
    twitter_field_sel = (By.ID, "twitter")
    unknownbd_radio_sel = (By.ID, "birthdateApproximate_unknown")
    approxbd_radio_sel = (By.ID, "birthdateApproximate_approximate")
    approxbd_num_sel = (By.ID, "age")
    exactbd_radio_sel = (By.ID, "birthdateApproximate_exact")
    exactbd_date_sel = (By.ID, "specificDate")
    isdeceased_check_sel = (By.ID, "markPersonDeceased")
    knowdeceasedate_check_sel = (By.ID, "checkboxDatePersonDeceased")
    deceasedatereminder_check_sel = (By.ID, "addReminderDeceased")
    deceaseyear_select_sel = (By.ID, "year")
    deceasemonth_select_sel = (By.ID, "month")
    deceaseday_select_sel = (By.ID, "day")

    def delete_this_contact(self):
        delete_btn = self.driver.find_element(*self.delete_btn_sel)
        delete_btn.click()
        Alert(self.driver).accept()
        from .contacts import ContactsPage
        return ContactsPage(self.driver)

    def set_gender_male(self):
        male_radio = self.driver.find_element(*self.gender_male_radio_sel)
        male_radio.click()

    def set_gender_none(self):
        none_radio = self.driver.find_element(*self.gender_none_radio_sel)
        none_radio.click()

    def set_gender_female(self):
        female_radio = self.driver.find_element(*self.gender_female_radio_sel)
        female_radio.click()

    def set_first_name(self, fname):
        field = self.driver.find_element(*self.first_name_field_sel)
        field.clear()
        field.send_keys(fname)

    def set_last_name(self, lname):
        field = self.driver.find_element(*self.last_name_field_sel)
        field.clear()
        field.send_keys(lname)

    def set_street(self, sname):
        street = self.driver.find_element(*self.street_field_sel)
        street.clear()
        street.send_keys(sname)

    def set_city(self, cname):
        city = self.driver.find_element(*self.city_field_sel)
        city.clear()
        city.send_keys(cname)

    def set_province(self, pname):
        prov = self.driver.find_element(*self.province_field_sel)
        prov.clear()
        prov.send_keys(pname)

    def set_postcode(self, pcode):
        postcode = self.driver.find_element(*self.postcode_field_sel)
        postcode.clear()
        postcode.send_keys(pcode)

    def choose_from_multiselect(self, select_tag, choice):
        opts = select_tag.find_elements_by_tag_name("option")
        for opt in opts:
            if opt.text.strip() == choice:
                opt.click()
                return
        raise OptionNotFoundException("No such option %s" % choice)

    def set_country(self, cname):
        country = self.driver.find_element(*self.country_selector_sel)
        self.choose_from_multiselect(country, cname)

    def set_email_address(self, ename):
        email = self.driver.find_element(*self.email_field_sel)
        email.clear()
        email.send_keys(ename)

    def set_phone(self, pname):
        phone = self.driver.find_element(*self.phone_field_sel)
        phone.clear()
        phone.send_keys(pname)

    def set_facebook(self, fname):
        fb = self.driver.find_element(*self.facebook_field_sel)
        fb.clear()
        fb.send_keys(fname)

    def set_twitter(self, tname):
        tw = self.driver.find_element(*self.twitter_field_sel)
        tw.clear()
        tw.send_keys(tname)

    def set_dont_know_age(self):
        ubd = self.driver.find_element(*self.unknownbd_radio_sel)
        ubd.click()

    def set_probable_age(self, page):
        abd = self.driver.find_element(*self.approxbd_radio_sel)
        abd.click()
        aval = self.driver.find_element(*self.approxbd_num_sel)
        aval.clear()
        aval.send_keys(page)

    def set_birthdate(self, bdate):
        bde = self.driver.find_element(*self.exactbd_radio_sel)
        bde.click()
        date = self.driver.find_element(*self.exactbd_date_sel)
        date.send_keys(bdate)

    def set_deceased_status(self, isdeceased):
        check = self.driver.find_element(*self.isdeceased_check_sel)
        if check.is_selected() != isdeceased:
            check.click()

    def set_is_deceased(self):
        self.set_deceased_status(True)

    def set_is_not_deceased(self):
        self.set_deceased_status(False)

    def set_know_deceased_date_status(self, know_deceased_date):
        check = self.driver.find_element(*self.knowdeceasedate_check_sel)
        if check.is_selected() != know_deceased_date:
            check.click()

    def set_dont_know_deceased_date(self):
        self.set_know_deceased_date_status(False)

    def set_know_deceased_date(self):
        self.set_know_deceased_date_status(True)

    def set_deceased_date(self, month, date, year):
        year_tag = self.driver.find_element(*self.deceaseyear_select_sel)
        self.choose_from_multiselect(year_tag, year)
        month_tag = self.driver.find_element(*self.deceasemonth_select_sel)
        self.choose_from_multiselect(month_tag, month)
        date_tag = self.driver.find_element(*self.deceaseday_select_sel)
        self.choose_from_multiselect(date_tag, date)

    def set_add_deceased_reminder_status(self, add_reminder):
        check = self.driver.find_element(*self.deceasedatereminder_check_sel)
        if check.is_selected() != add_reminder:
            check.click()

    def set_add_deceased_reminder(self):
        self.set_add_deceased_reminder_status(True)

    def set_dont_add_deceased_reminder(self):
        self.set_add_deceased_reminder_status(False)

    def click_cancel_button(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.cancel_button_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)

    def click_save_button(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.save_button_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)
