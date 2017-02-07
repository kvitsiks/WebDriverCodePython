import unittest
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.keys import Keys


class myClass (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_loop(self):
        driver = self.driver
        driver.get("https://www.portnov.com/")
        all_links = driver.find_elements_by_tag_name("a")
        for each_link in all_links:
            print each_link.text
            print each_link.get_attribute("href")
            # driver.back()





    # def tearDown(self):
    #     self.driver.close()

if __name__ == '__main__':
    unittest.main()
