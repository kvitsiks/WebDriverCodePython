# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lib.common import login, logout


class SortingTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://hrm.seleniumminutes.com"

    def test_sort_by_lastName(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        driver.get(self.base_url)

        self.assertEqual("OrangeHRM", driver.title)
        login(driver, "admin")
        driver.find_element_by_css_selector("#menu_pim_viewPimModule > b").click()

        driver.find_element_by_link_text("Last Name").click()

        wait.until(EC.presence_of_element_located(
                (By.XPATH, '//a[text()="Last Name" and @class="ASC"]')
        ))

        previous = ""
        while True:

            all_last_names = driver.find_elements_by_xpath(
            '//table[@id="resultTable"]//td[4]/a')

            for last_name_element in all_last_names:
                current = last_name_element.text.lower()

                self.assertLessEqual(
                        previous,
                        current,
                        'Expected last name {0} to be alphabetically same or before {1}'.format(
                            previous, current
                        )
                )


                # We are storing the current value for the future (into previous variable)
                previous = current

            pagination = driver.find_element_by_css_selector('ul.paging>li:first-child').text
            pages_description = pagination.split()
            last_page = pages_description[-1] in pages_description[0]

            # if not last_page:
            #     driver.find_element_by_link_text("Next").click()
            # else:
            #     break

            if last_page: break

            driver.find_element_by_link_text("Next").click()



        logout(driver)
        self.assertEqual("OrangeHRM", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
