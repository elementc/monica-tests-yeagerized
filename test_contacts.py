import unittest
from selenium import webdriver
from pages.login import LoginPage
class TestContacts(unittest.TestCase):
    def test_all_contacts_features(self):
        # setup and login
        d = webdriver.Chrome()
        d.get("https://app.monicahq.com/")
        login = LoginPage(d)
        dash = login.log_in_correctly()
        contacts = dash.go_contacts()

        # test adding a person
        add_person = contacts.click_add_person()
        contacts = add_person.click_cancel_button()
        add_person = contacts.click_add_person()
        add_person.set_first_name("Amanda")
        add_person.set_last_name("FictitiousName")
        add_person.set_gender_male()
        add_person.set_gender_none()
        add_person.set_gender_female()
        amanda = add_person.click_add_button()

        # test editing a person's details
        amanda = amanda.click_edit_contact()
        amanda = amanda.click_cancel_button()
        amanda = amanda.click_edit_contact()
        amanda.set_first_name("Mandy")
        amanda.set_last_name("FakeName")
        amanda.set_gender_male()
        amanda.set_gender_none()
        amanda.set_gender_female()
        amanda.set_street("150 W. University Blvd.")
        amanda.set_city("Melbourne")
        amanda.set_province("Florida")
        amanda.set_postcode("32901")
        amanda.set_country("United States")
        amanda.set_email_address("cdoran2011@my.fit.edu")
        amanda.set_phone("+13216748000")
        amanda.set_facebook("https://www.facebook.com/FloridaInstituteofTechnology/")
        amanda.set_twitter("https://twitter.com/floridatech")
        amanda.set_probable_age("20")
        amanda.set_birthdate("02021997")
        amanda.set_is_deceased()
        amanda.set_know_deceased_date()
        amanda.set_deceased_date("October", "30", "2017")
        amanda.set_add_deceased_reminder()
        amanda = amanda.click_save_button()
        assert "Mandy FakeName" in d.page_source
        # other asserts could be added here

        # test adding notes
        note = amanda.click_add_note()
        amanda = note.click_cancel()
        note = amanda.click_add_note()
        note.set_note_text("Has a weird obsession with panthers.")
        amanda = note.click_add_note()
        assert "panthers" in d.page_source

        # test logging activity
        activity = amanda.click_add_activity()
        amanda = activity.click_cancel()
        activity = amanda.click_add_activity()
        activity.set_description("went to a spacex landing and picnic")
        activity.set_date("12212015")
        activity.set_category("picknicked")
        activity.set_comment("I believe this will be, in retrospect, a major scientific acheivement.")
        amanda = activity.click_record_activity()
        assert "spacex" in d.page_source

        # test debt logger
        debt = amanda.click_add_debt()
        amanda = debt.click_cancel()
        debt = amanda.click_add_debt()
        debt.set_amount("13")
        debt.set_reason("went for hotdogs at sonic")
        debt.click_add_debt()
        assert "hotdogs" in d.page_source

        # test task adding
        task = amanda.click_add_task()
        amanda = task.click_cancel()
        task = amanda.click_add_task()
        task.set_task("email about her thesis")
        task.set_comment("you did want a copy, after all")
        amanda = task.click_add_task()
        assert "thesis" in d.page_source

        # clean up
        amanda = amanda.click_edit_contact()
        amanda.delete_this_contact()

if __name__ == '__main__':
    unittest.main()
