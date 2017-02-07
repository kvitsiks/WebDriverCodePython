import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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

        driver.find_element_by_id("menu_leave_viewLeaveModule").click()

        entitlements_menu_item = driver.find_element_by_id("menu_leave_Entitlements")
        view_leave_entitlements = driver.find_element_by_id("menu_leave_viewLeaveEntitlements")

        action = ActionChains(driver)
        action.move_to_element(
                entitlements_menu_item).move_to_element(view_leave_entitlements).click().perform()

        # # Another way
        # action.move_to_element(
        #         entitlements_menu_item).click(view_leave_entitlements)
        # action.perform()
        #
        # # Third way to do it
        # action.move_to_element(entitlements_menu_item)
        # action.move_to_element(view_leave_entitlements)
        # action.click()
        # action.perform()
        #
        # # If the connection is SLOW:
        # action.move_to_element(entitlements_menu_item).perform()
        # wait.until(
        #         expected_conditions.visibility_of(view_leave_entitlements))
        # action.click(view_leave_entitlements).perform()

        self.assertTrue(driver.find_element_by_tag_name('h1').text == "Leave Entitlements")

        time.sleep(1)
        type(driver, By.ID, "entitlements_employee_empName", "Bob Smith")

        wait.until(expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, ".ac_results strong"))).click()

        Select(driver.find_element_by_id("entitlements_leave_type")
               ).select_by_visible_text("Vacation")

        driver.find_element_by_id("searchBtn").click()

        self.assertTrue(driver.find_element_by_id("resultTable").is_displayed())

        logout(driver)

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()




    # def tearDown(self):
    #     self.driver.quit()
