import unittest
from selenium import webdriver
import pages

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")

    def test_google_search(self):
        google = pages.GooglePage(self.driver)
        searchresults = google.search("Red hot chili peppers")
        self.assertIn("Red hot chili peppers".lower(), searchresults.results[2].text.lower())
        searchresults.search_from_results_page("Nick Cave")
        self.assertIn("Nick Cave".lower(), searchresults.results[5].text.lower())
        self.assertNotIn("Red hot chili peppers".lower(), searchresults.results[6].text.lower())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
