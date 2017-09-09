import unittest
from selenium import webdriver
from pages.login import LoginPage
class TestContacts(unittest.TestCase):
    def test_login(self):
        d = webdriver.Chrome()
        d.get("https://app.monicahq.com/")
        login = LoginPage(d)
        login.log_in_correctly()

if __name__ == '__main__':
    unittest.main()
