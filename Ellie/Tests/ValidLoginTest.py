# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from lib.common import login, logout


class ValidLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hrm.seleniumminutes.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_valid_login(self):
        driver = self.driver

        driver.get(self.base_url + "/symfony/web/index.php/auth/login")
        self.assertEqual("OrangeHRM", driver.title)

        login(driver)
        self.assertEqual("Welcome Admin", driver.find_element_by_id("welcome").text)
        logout(driver)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
