from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


import json
import pytest


class page_1:

    def __init__(self,driver):
        self.driver = driver
        self.user_email_locator = (By.ID,"user_email")
        self.user_password_locator = (By.ID,"user_password")
        self.submit_to_login_locator = (By.XPATH,"//button[@type='submit']")

    def login_to_account(self,url,email,password):
        self.driver.get(url)
        self.driver.find_element(*self.user_email_locator).send_keys(email)
        self.driver.find_element(*self.user_password_locator).send_keys(password)
        self.driver.find_element(*self.submit_to_login_locator).click()

