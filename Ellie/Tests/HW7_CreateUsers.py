# -*- coding: utf-8 -*-
import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from lib.common import *


def get_random_string(max_str_length, min_str_length=2):
    str = ''

    chars = list('abcdefghijklmnopqrstuvwxyz')
    name_length = random.randrange(min_str_length, max_str_length + 1)

    for i in range(name_length):
        str += random.choice(chars)

    return str.title()



class HW7CreateUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hrm.seleniumminutes.com"
        self.driver.get(self.base_url)
        self.f = Faker()

    
    def test_h_w7_create_users(self):
        code = random.randrange(10000000, 100000000)
        # first_name = get_random_string(7)
        # last_name = get_random_string(10, 3)

        first_name = self.f.first_name()
        last_name = self.f.last_name()

        driver = self.driver

        login(driver)

        driver.find_element_by_css_selector("#menu_pim_viewPimModule > b").click()
        driver.find_element_by_id("btnAdd").click()

        type(driver, By.ID, "firstName", first_name)
        type(driver, By.ID, "lastName", last_name)
        type(driver, By.ID, "employeeId", code)

        driver.find_element_by_id("btnSave").click()

        driver.find_element_by_id("menu_admin_viewAdminModule").click()
        driver.find_element_by_id("btnAdd").click()

        type(driver, By.ID, "systemUser_employeeName_empName", "{0} {1}".format(first_name, last_name))

        type(driver, By.ID, "systemUser_userName", first_name + last_name)

        type(driver, By.ID, "systemUser_password", code)

        type(driver, By.ID, "systemUser_confirmPassword", code)

        driver.find_element_by_id("btnSave").click()

        wait = WebDriverWait(driver, 30)

        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@id='frmList_ohrmListComponent']/div[2]")))
        self.assertEqual("Successfully Saved\nClose", element.text)

        logout(driver)

        login(driver, first_name + last_name, code)

        self.assertEqual("Welcome " + first_name, driver.find_element_by_id("welcome").text)

        logout(driver)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
