import time
from driver import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

"""This class parent all pages"""


class Basepage():
    # This is my Locators for all pages
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    # def is_enabled(self,by_locator):
    #     element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
    #     return bool(element)

    # def is_d(self,by_locator):
    #     element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
    #     return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator):
        element1 = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element1)
