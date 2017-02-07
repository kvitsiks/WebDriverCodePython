import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import logging
import re

class Amazon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_amazon(self):
        driver = self.driver



        driver.get('https://www.amazon.com')
        myint = quantity = driver.find_element_by_xpath("//span[@id='nav-cart-count']").text
        print ("Old cart total is " + quantity)
        driver.find_element_by_id("twotabsearchtextbox").send_keys("apples in books")
        driver.find_element_by_xpath("//input[@value='Go']").click()
        #click on book
        driver.find_element_by_xpath(".//*[@id='result_0']/div/div/div/div[2]/div[2]/a/h2").click()
        #read the price
        x = driver.find_element_by_xpath(".//*[@id='buyNewSection']/a/h5/div/div[2]/div/span[2]").text
        price_for_one = x.replace("$","")
        print ("Price for 1 is: " + price_for_one)
        #change the quantity
        driver.find_element_by_id('quantity').click

        element = driver.find_element_by_xpath(".//*[@id='quantity']/option[5]")
        hover = ActionChains(driver).move_to_element(element).perform()
        element.click()

        driver.find_element_by_id("add-to-cart-button").click()
        time.sleep(1)
        myint = quantity1 = driver.find_element_by_id('nav-cart-count').text
        print ("New cart total is " + quantity1)

        # read the total
        y = driver.find_element_by_xpath(".//*[@id='hlb-subcart']/div[1]/span/span[2]").text
        price_for_five = y.replace("$","")
        print ("Price for 5 is: " + price_for_five)

        #strings to float
        price_for_one_float = float(price_for_one)
        price_for_five_float = float(price_for_five)
        quantity_int = int(quantity)
        quantity1_int = int(quantity1)

        if (price_for_one_float < price_for_five_float):
            print ("Test passed, the price is correct");
        else:
            print ("Test failed, the price is incorrect");


        if quantity1_int - quantity_int == quantity1_int:
            print ("Test1 passed, the quantity is correct")
        else:
            print ("Test1 failed, the quantity is incorrect")
        a = price_for_one_float * quantity1_int
        if (a == price_for_five_float):
            print a
            print ("Success!")
        else:
            print ("You are loser :(")

        driver.find_element_by_id("hlb-view-cart-announce").click()
        driver.find_element_by_xpath(".//*[@id='activeCartViewForm']/div[2]/div/div[4]/div[2]/div[1]/div/div/div[2]/div/span[1]/span/input").click()
        time.sleep(2)
        c = driver.find_element_by_xpath(".//*[@id='activeCartViewForm']/div[3]/p/span").text
        b = re.findall(r'\d+', c)
        print b
        print ("Your Subtotal is: "+b[0])
        b_int = int(b[0])
        if (b_int == quantity_int):
            print ("Passed: Subtotal = Cart count")
        else:
            print ("Error")






        # def tearDown(self):
        # self.driver.close()


















        #adding aditional 4 books into the cart and asserting the counter
        # driver.find_element_by_xpath("//a[@id='hlb-view-cart-announce']").click()
        # driver.find_element_by_xpath(".//*[@id='a-autoid-2-announce']").click()
        # driver.find_element_by_xpath(".//*[@id='dropdown1_3']").click()
        # time.sleep(2)
        # element2 = driver.find_element_by_id('nav-cart-count').text
        # print ("NewNew cart total is " + element2)
        # element2_int = int(element2)
        # if element2_int - element1_int == 3:
        #     print ("Test2 passed")
        # else:
        #     print ("Test2 failed")
        #
        # #hover a mouse
        # hover_element = driver.find_element_by_xpath(".//span[contains(text(),'Hello')]")
        # ActionChains(driver).move_to_element(hover_element).perform()
        # time.sleep(1)
        # driver.find_element_by_xpath(".//span[contains(text(),'Your Amazon Drive')]").click()
        # some_text = driver.find_element_by_xpath(".//*[@id='ap_signin1a_email_section_title']/h2")
        # assert "What is your email" in some_text.text
        # print some_text.text











