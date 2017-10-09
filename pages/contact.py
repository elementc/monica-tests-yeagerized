from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class ContactPage(HeaderPage):
    edit_contact_info_sel = (By.LINK_TEXT, "Edit contact information")
    def click_edit_contact(self) -> 'EditContactPage':
        btn = self.driver.find_element(*self.edit_contact_info_sel)
        btn.click()
        from .edit_contact import EditContactPage
        return EditContactPage(self.driver)
