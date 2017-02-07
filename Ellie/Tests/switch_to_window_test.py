import unittest

from selenium import webdriver

from lib.common import login


class SwitchWindowsTestCase(unittest.TestCase):
    def setUp(self):
        base_url = "http://hrm.seleniumminutes.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.get(base_url)
        self.driver = driver


    def tearDown(self):
        self.driver.quit()

    def test_switch_to_hrm_window(self):
        driver = self.driver

        login(driver)

        self.assertEqual(
                "Dashboard",
                driver.find_element_by_css_selector(".box>.head>h1").text
        )

        driver.find_element_by_css_selector("#branding>a:first-child").click()

        driver.switch_to.window(driver.window_handles[-1])

        self.assertEqual("https://www.orangehrm.com/", driver.current_url)
        actual = driver.find_element_by_css_selector("h1#firstline strong").text
        self.assertEqual("3 Million", actual)

        driver.switch_to.window(driver.window_handles[0])

        self.assertTrue(driver.find_element_by_id("welcome").text == "Welcome Admin")