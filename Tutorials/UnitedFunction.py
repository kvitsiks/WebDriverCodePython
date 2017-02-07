import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import logging
import re


class UnitedFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    def test_find_price(self,fromDest,toDest):
        driver = self.driver
        driver.get('https://www.united.com')
        driver.find_element_by_id("Origin").send_keys(fromDest)
        driver.find_element_by_id("Destination").send_keys(toDest)
        driver.find_element_by_id("DepartDate").send_keys("01/01/2017")
        driver.find_element_by_id("ReturnDate").send_keys("01/07/2017")
        driver.find_element_by_id("flightBookingSubmit").click()
        # driver.implicitly_wait(3)
        assert "Economy (lowest)" in driver.find_element_by_name("Economy (lowest)")
        assert "Flight Search Results | United Airlines" in driver.title
        # assert "$94" in driver.find_element_by_class_name("fare-wheel-item-fare")

    total1 = test_find_price("","SFO", "LAX")
    print ("SFO-JFK = " + total1)
    total2 = test_find_price("","SFO", "BOS")
    print ("SFO-JFK = " + total2)
    if (total1 == total2):
        print ("Price is the same");
    elif (total1 < total2):
        print ("SFO-JFK is a cheapest flight");
    else:
        print ("SFO-BOS is a cheapest flight");

