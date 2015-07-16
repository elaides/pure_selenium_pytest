import unittest
from selenium import webdriver
import pages

class NegativeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")

    def test_incorrect_login(self):
        google = pages.GooglePage(self.driver)
        login = google.go_to_login_page()
        login.login_with_incorrect_credentials("chornuj@gmail.com", "sdfs ")
        self.assertIsNotNone(login.error_message)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()