from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class ContactPage(HeaderPage):
    edit_contact_info_sel = (By.LINK_TEXT, "Edit contact information")
    add_note_sel = (By.LINK_TEXT, "Add another note")
    add_activity_sel = (By.LINK_TEXT, "Add activity")
    add_debt_sel = (By.LINK_TEXT, "Add debt")
    add_task_sel = (By.LINK_TEXT, "Add a task")

    def click_edit_contact(self) -> 'EditContactPage':
        btn = self.driver.find_element(*self.edit_contact_info_sel)
        btn.click()
        from .edit_contact import EditContactPage
        return EditContactPage(self.driver)

    def click_add_note(self) -> 'AddNotePage':
        btn = self.driver.find_element(*self.add_note_sel)
        btn.click()
        from .add_a_note import AddNotePage
        return AddNotePage(self.driver)

    def click_add_activity(self) -> 'AddActivityPage':
        btn = self.driver.find_element(*self.add_activity_sel)
        btn.click()
        from .add_an_activity import AddActivityPage
        return AddActivityPage(self.driver)

    def click_add_debt(self) -> 'AddDebtPage':
        btn = self.driver.find_element(*self.add_debt_sel)
        btn.click()
        from .add_a_debt import AddDebtPage
        return AddDebtPage(self.driver)

    def click_add_task(self) -> 'AddTaskPage':
        btn = self.driver.find_element(*self.add_task_sel)
        btn.click()
        from .add_a_task import AddTaskPage
        return AddTaskPage(self.driver)
