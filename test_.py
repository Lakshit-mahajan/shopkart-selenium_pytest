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

from page_object_model import page_1

data_file = "C:/Users/ASUS/Downloads/python/kart/data.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_list = data_file_python["data"]

class Test_all_functions:

    @pytest.mark.parametrize("data",data_list)
    def test_get_page(self,browser_fixture,data):
        self.driver = browser_fixture
        get_kart = page_1.page1(self.driver)
        get_kart.get_product_page(data["url"])


