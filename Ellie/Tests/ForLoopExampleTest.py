# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver


class ForLoopExampleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hrm.seleniumminutes.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_valid_login(self):
        driver = self.driver

        driver.get(self.base_url + "/symfony/web/index.php/auth/login")
        self.assertEqual("OrangeHRM", driver.title)
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("Password")
        driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", driver.title)

        icon_locator = ".quickLaunge img"

        images = driver.find_elements_by_css_selector(icon_locator)
        for image in images:
            size = image.size
            self.assertEqual(size['width'], 50)
            self.assertEqual(size['height'], 50)

        self.assertEqual("Welcome Admin", driver.find_element_by_id("welcome").text)
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()
        self.assertEqual("OrangeHRM", driver.title)

    def test_add(self):
        self.assertTrue(5+7 == 12)
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
