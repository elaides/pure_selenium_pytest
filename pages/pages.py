from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def s(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def ss(self, locator):
        return self.driver.find_elements_by_css_selector(locator)


class GooglePage(BasePage):
    def search_for(self, text):
        self.s("#lst-ib").send_keys(text)
        self.s("#sblsbb").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ires .g .r>a')))
        return SearchResultsPage(self.driver)

    def go_to_login_page(self):
        self.s("#gb_70").click()
        return LoginPage(self.driver)

    def logged_user(self):
        return self.s("a.gb_pa.gb_l.gb_r").get_attribute("title")


class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super(SearchResultsPage, self).__init__(driver)
        self.results = self.ss("#ires .g .r>a")

    def search_for(self, text):
        self.s("#lst-ib").clear()
        self.s("#lst-ib").send_keys(text)
        self.s(".lsb").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ires .g .r>a')))
        self.results = self.ss("#ires .g .r>a")
        return self.results


class LoginPage(BasePage):
    def enter_email(self, email):
        self.s("#Email").send_keys(email)
        self.s("#next").click()

    def enter_password(self, password):
        self.s("#Passwd").send_keys(password)
        self.s("#signIn").click()

    def error_message(self):
        return self.s("#errormsg_0_Passwd")