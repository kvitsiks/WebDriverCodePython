# -*- coding: utf-8 -*-
import random
import unittest

from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lib.common import *


class HW4CreateUser(unittest.TestCase):

    def create_name(self, max_length):
        chars = list('abcdefghijklmnopqrstuvwxyz')
        number_of_chars_in_the_name = random.randrange(1, max_length+1)
        name = ''

        for i in range(number_of_chars_in_the_name):
            name += random.choice(chars)  # ## Same as name = name + random.choice(chars)
        return name.title()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hrm.seleniumminutes.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_h_w4_create_user(self):
        driver = self.driver
        driver.get(self.base_url + "/symfony/web/index.php/auth/login")
        login(driver)
        driver.find_element_by_css_selector("#menu_pim_viewPimModule > b").click()
        driver.find_element_by_id("btnAdd").click()

        firstName = self.create_name(7)
        enter_text(driver, By.ID, "firstName", firstName)

        lastName = self.create_name(10)
        enter_text(driver, By.ID, "lastName", lastName)

        code = random.randrange(10000000, 100000000)
        enter_text(driver, By.ID, "employeeId", code)

        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_css_selector("b").click()
        # driver.find_element_by_id("menu_admin_viewSystemUsers").click()
        driver.find_element_by_id("menu_admin_viewAdminModule").click()
        driver.find_element_by_id("btnAdd").click()

        enter_text(driver, By.ID, "systemUser_employeeName_empName", firstName + " " + lastName)

        username = firstName + lastName

        enter_text(driver, By.ID, "systemUser_userName", username)
        enter_text(driver, By.ID, "systemUser_password", code)
        enter_text(driver, By.ID, "systemUser_confirmPassword", code)

        driver.find_element_by_id("btnSave").click()

        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//form[@id='frmList_ohrmListComponent']/div[2]")
        ))

        # for i in range(60):
        #     try:
        #         if driver.find_element_by_xpath("//form[@id='frmList_ohrmListComponent']/div[2]").is_displayed(): break
        #     except: pass
        #     time.sleep(1)
        # else: self.fail("time out")

        self.assertEqual("Successfully Saved\nClose", driver.find_element_by_xpath("//form[@id='frmList_ohrmListComponent']/div[2]").text)
        logout(driver)

        login(driver, username, code)
        self.assertEqual("Welcome " + firstName, driver.find_element_by_id("welcome").text)
        logout(driver)

    def test_FakerDemo(self):
        f = Faker()

        driver = self.driver
        driver.get(self.base_url + "/symfony/web/index.php/auth/login")
        login(driver)
        driver.find_element_by_css_selector("#menu_pim_viewPimModule > b").click()
        driver.find_element_by_id("btnAdd").click()

        firstName = f.first_name()
        enter_text(driver, By.ID, "firstName", firstName)

        lastName = f.last_name()
        enter_text(driver, By.ID, "lastName", lastName)

        code = f.ean(length=8)
        enter_text(driver, By.ID, "employeeId", code)

        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_css_selector("b").click()
        # driver.find_element_by_id("menu_admin_viewSystemUsers").click()
        driver.find_element_by_id("menu_admin_viewAdminModule").click()
        driver.find_element_by_id("btnAdd").click()

        enter_text(driver, By.ID, "systemUser_employeeName_empName", firstName + " " + lastName)

        username = firstName + lastName

        enter_text(driver, By.ID, "systemUser_userName", username)
        enter_text(driver, By.ID, "systemUser_password", code)
        enter_text(driver, By.ID, "systemUser_confirmPassword", code)

        driver.find_element_by_id("btnSave").click()

        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//form[@id='frmList_ohrmListComponent']/div[2]")
        ))

        self.assertEqual("Successfully Saved\nClose", driver.find_element_by_xpath("//form[@id='frmList_ohrmListComponent']/div[2]").text)
        logout(driver)

        login(driver, username, code)
        self.assertEqual("Welcome " + firstName, driver.find_element_by_id("welcome").text)
        logout(driver)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
