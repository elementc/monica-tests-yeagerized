from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class AddActivityPage(HeaderPage):
    activity_description_sel = (By.ID, "summary")
    activity_date_sel = (By.ID, "date_it_happened")
    activity_category_sel = (By.ID, "activity_type_id")
    activity_comment_sel = (By.ID, "description")
    record_activity_sel = (By.CSS_SELECTOR, ".actions button.btn-primary")
    cancel_button_sel = (By.LINK_TEXT, "Cancel")

    def set_description(self, desc):
        description = self.driver.find_element(*self.activity_description_sel)
        description.clear()
        description.send_keys(desc)

    def set_date(self, date):
        occured = self.driver.find_element(*self.activity_date_sel)
        occured.send_keys(date)

    def set_category(self, cat):
        cats = self.driver.find_element(*self.activity_category_sel)
        self.choose_from_multiselect(cats, cat)

    def set_comment(self, comm):
        comment = self.driver.find_element(*self.activity_comment_sel)
        comment.clear()
        comment.send_keys(comm)

    def click_record_activity(self) -> 'ContactPage':
        rec = self.driver.find_element(*self.record_activity_sel)
        rec.click()
        from .contact import ContactPage
        return ContactPage(self.driver)

    def click_cancel(self) -> 'ContactPage':
        cancel = self.driver.find_element(*self.cancel_button_sel)
        cancel.click()
        from .contact import ContactPage
        return ContactPage(self.driver)
