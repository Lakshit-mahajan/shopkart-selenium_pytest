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


class page_2:

    def __init__(self,driver):
        self.driver = driver
        self.open_hubstaff_task_locator = (By.XPATH,"//div[@class='row row-apps']/div[2]/div/a")


    def open_hubstaff_task(self):
        self.driver.find_element(*self.open_hubstaff_task_locator).click()
