import selenium.webdriver.support.ui as UI
import unittest
from selenium import webdriver

class myClass (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

def test(self):
    driver = self.driver
    driver.get("https://www.portnov.com/")
    wait = UI.WebDriverWait(driver, 5000)
    links = driver.find_elements_by_link_text("#/user/")
    for link in links:
        link.click()
        follow = driver.find_element_by_class_name("followAction")
        follow.click()
        driver.implicityly_wait(5)
        driver.back()