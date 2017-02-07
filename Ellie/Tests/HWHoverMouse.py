import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from lib.common import login, logout, type


class ActionChainDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hrm.seleniumminutes.com"

    def test_employee_entitlements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        driver.get(self.base_url)
        self.assertEqual("OrangeHRM", driver.title)

        login(driver)
        sleep(1)
        element = driver.find_element_by_xpath(".//*[@id='menu__Performance']/b")
        ActionChains(driver).move_to_element(element).perform()
        sleep(1)
        element2 = driver.find_element_by_xpath(".//*[@id='menu_performance_ManageReviews']")
        ActionChains(driver).move_to_element(element2).perform()
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='menu_performance_searchPerformancReview']").click()
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='btnAdd']").click()
        sleep(1)
        driver.find_element_by_id("saveReview360Form_employee").send_keys("Bob Smith")
        sleep(1)
        driver.find_element_by_xpath("html/body/div[5]/ul/li").click()
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='saveReview360Form_supervisorReviewer']").send_keys("John Smith")
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='saveReview360Form_workPeriodStartDate']").send_keys("2015-08-04")
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='saveReview360Form_workPeriodEndDate']").send_keys("2016-08-01")
        sleep(1)
        driver.find_element_by_xpath(".//*[@id='saveReview360Form_dueDate']").send_keys("2016-08-03")
        driver.find_element_by_xpath(".//*[@id='activateBtn']").click()
        driver.find_element_by_xpath(".//*[@id='saveBtn']").click()






        logout(driver)

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()