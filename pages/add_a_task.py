from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class AddTaskPage(HeaderPage):
    task_field_sel = (By.ID, "title")
    comment_field_sel = (By.ID, "description")
    add_task_sel = (By.CSS_SELECTOR, ".actions .btn-primary")
    cancel_sel = (By.LINK_TEXT, "Cancel")

    def set_task(self, task):
        field = self.driver.find_element(*self.task_field_sel)
        field.clear()
        field.send_keys(task)

    def set_comment(self, comment):
        comm = self.driver.find_element(*self.comment_field_sel)
        comm.clear()
        comm.send_keys(comment)

    def click_cancel(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.cancel_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)

    def click_add_task(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.add_task_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)
