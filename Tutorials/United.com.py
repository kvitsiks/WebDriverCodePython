import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import logging

class MyClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_my_test(self):
        driver = self.driver
        # driver.get('https://www.united.com')
        # driver.find_element_by_id("Origin").send_keys("SFO")
        # driver.find_element_by_id("Destination").send_keys("LAX")
        # driver.find_element_by_id("DepartDate").send_keys("01/01/2017")
        # driver.find_element_by_id("ReturnDate").send_keys("01/07/2017")
        # driver.find_element_by_id("flightBookingSubmit").click()
        # # driver.implicitly_wait(3)
        # assert "Economy (lowest)" in driver.find_element_by_name("Economy (lowest)")
        # assert "Flight Search Results | United Airlines" in driver.title
        # # assert "$94" in driver.find_element_by_class_name("fare-wheel-item-fare")

        driver.get('https://www.amazon.com')
        driver.find_element_by_id("twotabsearchtextbox").send_keys('Harry Potter: The Complete 8-Film Collection')
        driver.find_element_by_xpath("//input[@value='Go']").click()
        driver.find_element_by_xpath("//h2[@data-attribute='Harry Potter: The Complete 8-Film Collection by Warner Bros.']").click()
        driver.find_element_by_id("add-to-cart-button").click()
        assert "Amazon.com Shopping Cart" in driver.title
        print driver.title
        element1 = driver.find_element_by_id('nav-cart-count')
        assert element1.text == '1'
        print element1.text
        driver.back()
        driver.find_element_by_xpath("//img[@src='https://images-na.ssl-images-amazon.com/images/I/5124Pw9kXSL._AC_UL320_SR260,320_.jpg']").click()
        driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
        element2 = driver.find_element_by_id('nav-cart-count')
        assert element2.text == '2'
        print element2.text
        # self.assertAlmostEqual()
        driver.find_element_by_xpath("//a[@id='nav-cart']").click()
        driver.find_element_by_id("//div[@data-item-count='2']//span[@class='a-dropdown-prompt']").click()
        driver.find_element_by_xpath("//a[@id='dropdown4_1']").click()
        element3 = driver.find_element_by_id('nav-cart-count')
        assert element3.text == '3'
        print element3.text


    # def tearDown(self):
    #     self.driver.close()
