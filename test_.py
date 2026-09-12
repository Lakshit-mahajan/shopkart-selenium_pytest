from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

import json
import pytest
from page_object_model import page1
from page_object_model import page2

data_file = "C:/Users/ASUS/Downloads/python/hubstaff/hubstaff_/data.json"
with open(data_file,"r") as data_file:
    data_file_python = json.load(data_file)
    data_list = data_file_python["data"]

    

class Test_functions:

    @pytest.mark.login_page
    @pytest.mark.parametrize("data",data_list)
    def test_login(self,browser_fixture,data):
        self.driver = browser_fixture
        login = page1.page_1(self.driver)
        login.login_to_account(data["url"],data["email"],data["password"])

        hubstaff_task = page2.page_2(self.driver)
        hubstaff_task.open_hubstaff_task()


    @pytest.mark.go_to_hubstaff_task
    @pytest.mark.parametrize("data",data_list)
    def test_go_to_hubstaff_task(self,browser_fixture,data):
        self.driver = browser_fixture
        login = page1.page_1(self.driver)
        login.login_to_account(data["url"],data["email"],data["password"])
        
        hubstaff_task = page2.page_2(self.driver)
        hubstaff_task.open_hubstaff_task()






    

    
    
