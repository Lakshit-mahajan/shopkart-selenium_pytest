from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import json



class page1:

    def __init__(self,driver):
        self.driver = driver


    def get_product_page(self,url):
        self.driver.get(url)