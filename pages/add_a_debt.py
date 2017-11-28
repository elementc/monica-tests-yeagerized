from .header_page import HeaderPage
from selenium.webdriver.common.by import By

class AddDebtPage(HeaderPage):
    amount_sel = (By.ID, "amount")
    reason_sel = (By.ID, "reason")
    add_debt_sel = (By.CSS_SELECTOR, ".actions button.btn-primary")
    cancel_sel = (By.LINK_TEXT, "Cancel")
    # TODO: add radio for you owe them vs they owe you

    def set_amount(self, amount):
        owed = self.driver.find_element(*self.amount_sel)
        owed.clear()
        owed.send_keys(amount)

    def set_reason(self, reason):
        rea = self.driver.find_element(*self.reason_sel)
        rea.clear()
        rea.send_keys(reason)

    def click_cancel(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.cancel_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)

    def click_add_debt(self) -> 'ContactPage':
        btn = self.driver.find_element(*self.add_debt_sel)
        btn.click()
        from .contact import ContactPage
        return ContactPage(self.driver)
