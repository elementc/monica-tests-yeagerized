import unittest
from selenium import webdriver
from pages.login import LoginPage
class TestContacts(unittest.TestCase):
    def test_login(self):
        d = webdriver.Chrome()
        d.get("https://app.monicahq.com/")
        login = LoginPage(d)
        dash = login.log_in_correctly()
        contacts = dash.go_contacts()
        add_person = contacts.click_add_person()
        contacts = add_person.click_cancel_button()
        add_person = contacts.click_add_person()
        add_person.set_first_name("Amanda")
        add_person.set_last_name("FictitiousName")
        add_person.set_gender_male()
        add_person.set_gender_none()
        add_person.set_gender_female()
        amanda = add_person.click_add_button()
        amanda = amanda.click_edit_contact()
        amanda.delete_this_contact()

if __name__ == '__main__':
    unittest.main()
