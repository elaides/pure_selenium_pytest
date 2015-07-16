#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'Art'
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class GooglePage(BasePage):
    def search(self, text):
        self.driver.find_element_by_id("lst-ib").send_keys(text)
        self.driver.find_element_by_id("sblsbb").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ires .g .r>a')))
        return SearchResultsPage(self.driver)

    def go_to_login_page(self):
        self.driver.find_element_by_id("gb_70").click()
        return LoginPage(self.driver)

    def logged_user_is(self):
        return self.driver.find_element_by_css_selector("a.gb_pa.gb_l.gb_r").get_attribute("title")





class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super(SearchResultsPage, self).__init__(driver)
        self.results = self.driver.find_elements_by_css_selector("#ires .g .r>a")

    def search_from_results_page(self, text):
        self.driver.find_element_by_id("lst-ib").clear()
        self.driver.find_element_by_id("lst-ib").send_keys(text)
        self.driver.find_element_by_css_selector(".lsb").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#ires .g .r>a')))
        self.results = self.driver.find_elements_by_css_selector("#ires .g .r>a")
        return self.results


class LoginPage(BasePage):
    def enter_email(self, email):
        self.driver.find_element_by_id("Email").send_keys(email)
        self.driver.find_element_by_id("next").click()

    def enter_password(self, password):
        self.driver.find_element_by_id("Passwd").send_keys(password)
        self.driver.find_element_by_id("signIn").click()

    def login(self, email, password):
        self.enter_email(email)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID,'Passwd')))
        self.enter_password(password)
        return GooglePage(self.driver)

    def login_with_incorrect_credentials(self, email, password):
        self.enter_email(email)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID,'Passwd')))
        self.enter_password(password)

    def error_message(self):
        return self.driver.find_element_by_id("errormsg_0_Passwd")