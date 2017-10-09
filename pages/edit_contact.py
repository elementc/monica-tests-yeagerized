from .header_page import HeaderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class EditContactPage(HeaderPage):
    delete_btn_sel = (By.LINK_TEXT, "click here")

    def delete_this_contact(self):
        delete_btn = self.driver.find_element(*self.delete_btn_sel)
        delete_btn.click()
        Alert(self.driver).accept()
        from .contacts import ContactsPage
        return ContactsPage(self.driver)
