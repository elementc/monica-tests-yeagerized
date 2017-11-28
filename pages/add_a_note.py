from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class AddNotePage(HeaderPage):
    text_field_sel = (By.NAME, "body")
    add_note_button_sel = (By.CSS_SELECTOR, "button.btn-primary")
    cancel_button_sel = (By.CLASS_NAME, "btn-secondary")

    def set_note_text(self, text):
        tf = self.driver.find_element(*self.text_field_sel)
        tf.clear()
        tf.send_keys(text)

    # note: only returns a contact page if the note text, snipped, is not empty
    # otherwise returns the same page with an error message
    def click_add_note(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.add_note_button_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)

    def click_cancel(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.cancel_button_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)
