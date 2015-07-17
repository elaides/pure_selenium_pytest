import unittest

from selenium import webdriver

from pages import pages


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://accounts.google.com/ServiceLogin?hl=uk&continue=https://www.google.com.ua/#identifier")

    def test_login_with_incorrect_password(self):
        login_page = pages.LoginPage(self.driver)
        login_page.enter_email(email="chornuj@gmail.com")
        login_page.enter_password(password="sdf")
        assert login_page.error_message().is_displayed()
        login_page.enter_password(password="fh[b'gbcrjg1")
        logged_page = pages.GooglePage(self.driver)
        assert "chornuj@gmail.com" in logged_page.logged_user()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
