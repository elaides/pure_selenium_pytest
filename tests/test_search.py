import unittest

from selenium import webdriver

from pages import pages


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")

    def test_google_search(self):
        google = pages.GooglePage(self.driver)
        searchresults = google.search_for("Red hot chili peppers")
        assert "Red hot chili peppers".lower() in searchresults.results[2].text.lower()
        searchresults.search_for("Nick Cave")
        assert "Nick Cave".lower() in searchresults.results[5].text.lower()
        assert "Red hot chili peppers".lower() not in searchresults.results[6].text.lower()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
