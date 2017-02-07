import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import logging

class MyClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_my_test(self):
        driver = self.driver
# Python Exception Logging Module
#         LOG_FILENAME = 'example.log'
#         logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
#         logging.debug('Chrome instance started')
#         print(driver.capabilities['version'])
#         logging.debug('Browser version printed')

#  Python Selenium Webdriver Refresh a Webpage
#         driver.get("https://www.linkedin.com")
#         time.sleep(3)
#         driver.refresh()
#         time.sleep(2)

# Python Selenium Navigation Back Forward Button
#         driver.get("https://www.google.com")
#         elem = driver.find_element_by_link_text('About')
#         time.sleep(2)
#         elem.click()
#         time.sleep(3)
#         driver.back()
#         time.sleep(2)
#         driver.forward()

#Python Selenium WebDriver Scroll Down Page
        # driver.get("http://wikipedia.org")
        # elem = driver.find_element_by_tag_name('html')
        # elem.send_keys(Keys.END)
        # time.sleep(2)
        # elem.send_keys(Keys.HOME)

# Get Browser Version using Python Selenium
#         driver.get("http://wikipedia.org")
#         print("Ferefox Version is: " + driver.capabilities['version'])

# Open new tab in Firefox using Selenium WebDriver
#         driver.get("https://www.google.com")
#         elem = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

#Python Selenium Click Radio Button
        # driver.get("https://www.zkoss.org/zkdemo/input/radio_button")
        # for i in driver.find_elements_by_xpath("//*[@type='radio']"):
        #     i.click()
        # time.sleep(2)

        # driver.get("http://hrm.portnov.com")
        # login_field = driver.find_element_by_id("txtUsername").send_keys('peter')
        # password_field = driver.find_element_by_id("txtPassword").send_keys("sep16")
        # driver.find_element_by_id("btnLogin").click()
        # for i in driver.find_elements_by_xpath("//*[@name='chkSelectRow[]']"):
        #     i.click()
        #     # for i in driver.find_elements_by_xpath("//*[@name='chkSelectRow[]']"):
        #     #     i.click()
        # driver.find_element_by_link_text("2").click()
        # for i in driver.find_elements_by_xpath("//*[@name='chkSelectRow[]']"):
        #     i.click()
        # driver.back()

#Python Selenium Click on Checkbox (20 tries)
        # driver.get("http://hrm.portnov.com")
        # login_field = driver.find_element_by_id("txtUsername").send_keys('peter')
        # password_field = driver.find_element_by_id("txtPassword").send_keys("sep16")
        # driver.find_element_by_id("btnLogin").click()
        # for i in range (20):
        #     try:
        #         driver.find_element_by_xpath("//*[@id='ohrmList_chkSelectRecord_445']").click()
        #         break
        #     except NoSuchElementException as e:
        #         print("retry")
        #         driver.refresh()
        #         time.sleep(2)
        # else:
        #     print('Test failed')

#Python Selenium Re-size Maximize Window, POSITION
        # driver.get("http://wikipedia.org")
        # time.sleep(2)
        # driver.set_window_size(500,368)
        # time.sleep(2)
        # print(driver.get_window_size())
        # driver.set_window_position(200, 300)
        # time.sleep(2)
        # print(driver.get_window_position())

#Python Selenium Get HTML Page Source
        # driver.get("http://wikipedia.org")
        # html_source = driver.page_source
        # print(html_source)

#Assert Page Title in Python Selenium
        # driver.get("http://gogle.com")
        # try:
        #     assert 'Googled' in driver.title
        #     print("Test pass")
        # except Exception as e:
        #     print("Test failed")

#Python Selenium Switch to New Tab
        # driver.get("http://gogle.com")
        # body = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        # driver.get("http://www.bing.com")
        # time.sleep(2)
        # body = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        # driver.get("http://www.portnov.com")
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)
        # time.sleep(2)
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
        # time.sleep(2)

#Get text of Image element in Selenium Python (DOESN"T WORK
        # driver.get("http://wikipedia.org")
        # for element in driver.find_element_by_tag_name('img'):
        #     print(element.text)
        #     print(element.tag_name)
        #     print(element.location)
        #     print(element.size)

#Get text of element in Selenium Python WebDriver
        # driver.get("https://www.portnov.com/portnov-computer-school/home")
        # element = driver.find_element_by_xpath("//div[@class='field-item even']")
        # print (element.text)

#Right Click Context Menu Selenium Python
        # driver.get("https://en.wikipedia.org/wiki/Main_Page")
        # element = driver.find_element_by_link_text("Commons")
        # actionChains = ActionChains(driver)
        # actionChains.context_click(element).perform()
        # actionChains.send_keys(Keys.ARROW_DOWN).perform()
        # actionChains.send_keys(Keys.ENTER).perform()

#Mouse Hover Actions in Selenium Python Webdriver
        # driver.get("https://en.wikipedia.org/wiki/Main_Page")
        # element = driver.find_element_by_link_text("Community portal")
        # hover = ActionChains(driver).move_to_element(element)
        # hover.perform()

# Execute Javascript using Selenium Python
#         driver.get("https://en.wikipedia.org/wiki/Main_Page")
#         driver.execute_script("window.alert('Fuck you!!!');")
#         time.sleep(3)
#         alert = driver.switch_to_alert()
#         alert.accept()
#         alert.dismiss()

# Zoom In WebPage In Selenium Python
#         driver.get("https://en.wikipedia.org/wiki/Main_Page")
#         driver.execute_script("document.body.style.zoom='25%'")

#Selenium Python Select All Text on Page
        # driver.get("https://en.wikipedia.org/wiki/Main_Page")
        # element = driver.find_element_by_css_selector('body')
        # time.sleep(3)
        # element.send_keys(Keys.CONTROL+'a')
        # print (element.text)

        # driver.get("https://en.wikipedia.org/wiki/Main_Page")
        # element = driver.find_element_by_xpath("//li[@id='pt-anonuserpage']")
        # actionChains = ActionChains(driver)
        # actionChains.context_click(element).perform()
        # actionChains.send_keys(Keys.ARROW_DOWN).perform()
        # actionChains.send_keys(Keys.ARROW_DOWN).perform()
        # actionChains.send_keys(Keys.ENTER).perform()

#Selenium Python Actionchains Double Click
        # driver.get("https://en.wikipedia.org/wiki/Main_Page")
        # element = element = driver.find_element_by_xpath("//li[@id='pt-anonuserpage']")
        # actionchains = ActionChains(driver)
        # actionchains.double_click(element).perform()

#Selenium Python Get Element Size
        # driver.get("https://en.wikipedia.org/wiki/Main_Page")
        # element = driver.find_element_by_xpath("//img[@alt='Original Wembley Stadium']")
        # print(element.size)

#Selenium Python Element is displayed
        # driver.get("https://en.wikipedia.org/wiki/Main_Page")
        # element = driver.find_element_by_xpath("//img[@alt='Original Wembley Stadium']")
        # assert element.is_displayed()
        # print (element.is_displayed())

#Selenium Python Element is_Selected
        # driver.get("http://hrm.portnov.com")
        # driver.find_element_by_id("txtUsername").send_keys('peter')
        # driver.find_element_by_id("txtPassword").send_keys("sep16")
        # driver.find_element_by_id("btnLogin").click()
        # element = driver.find_element_by_id("ohrmList_chkSelectRecord_4454")
        # print (element.is_selected())






    def tearDown(self):
        time.sleep(3)
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
