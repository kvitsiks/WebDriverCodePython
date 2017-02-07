# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from lib.common import login, logout


class SearchByJobTitle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hrm.seleniumminutes.com"

    def test_search_for_qa_manager(self):
        driver = self.driver

        driver.get(self.base_url)

        self.assertEqual("OrangeHRM", driver.title)
        login(driver, "admin")

        driver.find_element_by_css_selector("#menu_pim_viewPimModule > b").click()
        Select(driver.find_element_by_id("empsearch_job_title")).select_by_visible_text(
            "QA Manager")
        driver.find_element_by_id("searchBtn").click()
        self.assertEqual("OrangeHRM", driver.title)

        # OPTION #1
        # retrieve 5th cell from all rows in the table
        all_results = driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr/td[5]")

        # loop through each resulting element
        for single_result in all_results:
            # check the text of each 5th cell to ensure in contains QA Manager
            self.assertEqual("QA Manager", single_result.text)

        # OPTION #2
        # retrieve all rows in the table
        all_rows = driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr")

        # loop through each resulting row
        for row in all_rows:
            # check the text of each 5th cell to ensure in contains QA Manager
            self.assertEqual("QA Manager", row.find_element_by_xpath('.//td[5]').text)

        logout(driver)
        self.assertEqual("OrangeHRM", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
