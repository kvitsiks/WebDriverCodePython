# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CalculatorClickNumber(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://chemistry.about.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_calculator_click_number(self):
        driver = self.driver
        driver.get(self.base_url + "/library/weekly/blcalculator.htm")
        # ERROR: Caught exception [ERROR: Unsupported command [getEval |  | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | Math.round(Math.random() * 9) | ]]
        print(num1)
        print(num2)
        driver.find_element_by_name("cal" + num1).click()
        driver.find_element_by_name("calplus").click()
        driver.find_element_by_name("cal" + num2).click()
        driver.find_element_by_name("calequal").click()
        # Check result using 2 lines
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | ${num1} + ${num2} | ]]
        self.assertEqual(result, driver.find_element_by_name("calcResults").get_attribute("value"))
        # Or using 1 line only
        # ERROR: Caught exception [ERROR: Unsupported command [getEval |  | ]]
        driver.find_element_by_name("calclear").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
