import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as ES

class myClass (unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test(self):
        driver = self.driver
        driver.get("http://demo.mahara.org/")
        login = driver.find_element_by_xpath("//input[@id ='login_login_username']")
        login.send_keys("student1")
        password = driver.find_element_by_xpath("//input[@id ='login_login_password']").send_keys("Testing1")
        driver.find_element_by_xpath("//input[@id='login_submit']").click()

    #def test(self):
        #driver = self.driver
        driver.find_element_by_xpath("//span[@class='icon icon-cogs']//following::span[@class='nav-title'][1]").click()
        max_field = driver.find_element_by_xpath("//input[@id = 'accountprefs_tagssideblockmaxtags']")
        max_field.clear()
        max_field.send_keys("30")
        max_field2 = driver.find_element_by_xpath("//input[@id = 'accountprefs_tagssideblockmaxtags']").get_attribute('value')
        driver.get_screenshot_as_file('C:\\Users\\Kvitsiks\\PycharmProjects\\Tutorials\\Screenshots\\Picture.png')
        print max_field2
        self.assertTrue(max_field2, "30")
        driver.find_element_by_xpath("//option[@value='http://creativecommons.org/licenses/by-nc/3.0/']").click()
        driver.find_element_by_id("accountprefs_submit").click()
        driver.get_screenshot_as_file('C:\\Users\\Kvitsiks\\PycharmProjects\\Tutorials\\Screenshots\\Picture1.png')

    #def test(self):
        #driver = self.driver
        sort_groups = driver.find_element_by_xpath("//option[text() ='Earliest joined']").get_attribute('value')
        print sort_groups
        self.assertTrue(sort_groups, "Earliest joined")


    def tearDown(self):
        self.driver.find_element_by_link_text("Logout").click()



    @classmethod
    def tearDown(self):
        self.driver.close()

