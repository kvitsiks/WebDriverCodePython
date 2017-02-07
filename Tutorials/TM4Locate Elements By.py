from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class myClass (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    # def test1(self):
    #     driver = self.driver
    #     driver.get("http://demo.mahara.org")
    #     username = driver.find_element(By.XPATH,"//input[@id ='login_login_username']").send_keys("Student1")
    #     password = driver.find_element(By.XPATH,"//input[@id ='login_login_password']").send_keys("Testing1")
    #     login = driver.find_element(By.XPATH,"//input[@id='login_submit']").click()
    #     driver.get_screenshot_as_file('C:\\Users\\Kvitsiks\\PycharmProjects\\Tutorials\\Screenshots\\Picture2.png')
    #     assert "Dashboard - Mahara" in driver.title
    #     print (driver.title)
    #     logout = driver.find_element(By.XPATH, "//span[@class='icon icon-cogs']//following::span[@class='nav-title'][2]").click()
    #     assert "Home - Mahara" in driver.title
    #     driver.get_screenshot_as_file('C:\\Users\\Kvitsiks\\PycharmProjects\\Tutorials\\Screenshots\\Picture3.png')
    #     print (driver.title)
    def test2(self):
        driver = self.driver
        driver.get("http://demo.mahara.org")
        all_links = driver.find_elements(By.TAG_NAME,"div")
        for each_link in all_links:
            print (each_link.get_attribute('id'))
        total_links = len(all_links)
        print (total_links)



    def tearDown(self):
        self.driver.close()