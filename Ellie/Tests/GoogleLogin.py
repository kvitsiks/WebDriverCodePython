from selenium import webdriver
from time import sleep

import unittest


class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_login_Google(self):
        self.browser.get("http://www.gmail.com")

        #TODO aasdfsadjfsdhfsadf
        login = self.browser.find_element_by_id("Email")
        login.send_keys("kvitsinskiys")
        click_login = self.browser.find_element_by_id("next")
        click_login.click()
        sleep(1)

        password = self.browser.find_element_by_id("Passwd")
        password.send_keys("Ksv1985=ksv")
        click_password = self.browser.find_element_by_id("signIn")
        click_password.click()

        logo_Google = self.browser.find_element_by_id(":j")
        print logo_Google.text
        sleep(1)
        menu = self.browser.find_element_by_xpath("//*[@id='gb']/div[1]/div[1]/div[2]/div[4]/div[1]/a/span")
        menu.click()
        sleep(1)
        logout = self.browser.find_element_by_xpath("//*[@id='gb_71']")
        print logout.text
        sleep(1)
        logout.click()

    def tearDown(self):
        self.browser.close()
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()