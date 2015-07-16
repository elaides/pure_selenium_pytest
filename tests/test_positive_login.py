import unittest
from selenium import webdriver
import pages

class PositiveTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")

    def test_login(self):
        google = pages.GooglePage(self.driver)
        logged_page = google.go_to_login_page().login("chornuj@gmail.com", "")   # your test credentials here
        self.assertIn("chornuj@gmail.com", logged_page.logged_user_is())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
