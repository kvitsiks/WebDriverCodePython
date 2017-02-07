from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from time import sleep

class myClass (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    def test1(self):
        driver = self.driver
        driver.get("http://www.zultys.com/")
        driver.find_element(By.XPATH,"//li[@id='nav-menu-item-5198']").click()
        sleep(1)
        assert "Contact Us :: ZULTYS Business Phone Solutions" in driver.title
        print (driver.title)
        driver.find_element_by_xpath("//input[@name = 'name']").send_keys("John")
        driver.find_element_by_xpath("//input[@name = 'email']").send_keys("ksv2@mail.ua")
        driver.find_element_by_xpath("//input[@name = 'city']").send_keys("Odessa")
        driver.find_element_by_xpath("//input[@name = 'company']").send_keys("PWC")
        driver.find_element_by_xpath("//input[@name = 'phone']").send_keys("8328676262")
        driver.find_element_by_xpath("//option[@value='USA-AK']").click()
        driver.find_element_by_xpath("//option[@value='Product Inquiry']").click()
        driver.find_element_by_xpath("//textarea[@name = 'message']").send_keys("Test. Zultys is a manufacturer of Voice-over-IP (VoIP) communications systems for organizations with 10-10,000 users, with corporate headquarters in Sunnyvale, California.")
        driver.get_screenshot_as_file('C:\\Users\\Kvitsiks\\PycharmProjects\\Tutorials\\Screenshots\\Picture1.png')
        message = driver.find_element_by_class_name("wpcf7-response-output wpcf7-display-none wpcf7-mail-sent-ok")
        print (driver.massage)
        driver.find_element_by_xpath("//p[10]/input").click()



    # def tearDown(self):
    #     self.driver.close()