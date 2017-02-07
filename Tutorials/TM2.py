import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as ES

class myNewClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    def test(self):
        driver = self.driver
        driver.get("http://demo.mahara.org")
        driver.find_element_by_id("login_login_username").send_keys("Student1")
        driver.find_element_by_id("login_login_password").send_keys("Testing1")
        driver.find_element_by_id("login_submit").click()
        assert "Dashboard - Mahara" in driver.title
        print (driver.title)
        driver.find_element_by_link_text("Logout").click()
        assert "Home - Mahara" in driver.title
        print (driver.title)


    def tearDown(self):
        self.driver.close()
