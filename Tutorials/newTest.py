import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_myUnitTest(self):
        driver = self.driver
        driver.get('http://hrm.seleniumminutes.com//')
        driver.maximize_window()
        #driver.set_page_load_timeout(20)
        driver.implicitly_wait(1)
        login_field = driver.find_element_by_id("txtUsername").send_keys('admin')
        password_field = driver.find_element_by_id("txtPassword").send_keys("Password")
        driver.find_element_by_id("btnLogin").click()
        driver.get_screenshot_as_file('C:\\Users\\Kvitsiks\\PycharmProjects\\Tutorials\\Screenshots\\Picture.png')
        print (driver.title)
        assert "OrangeHRM" in driver.title
        # images = driver.find_elements_by_xpath("//img[@class = 'alignnone  wp-image-85']")
        # for image in images:
        #     size = image.size
        #     self.assertEquals(size['width'], 212)
        #     self.assertEquals(size['height'], 159)

    def tearDown(self):
        self.driver.close()







if __name__ == '__main__':
    unittest.main()
