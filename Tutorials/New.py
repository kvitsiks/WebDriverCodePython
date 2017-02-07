from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.portnov.com')
driver.set_page_load_timeout(1)
assert 'Software Testing and Software QA Training classes in Bay Area | Portnov Computer School' in driver.title
print (driver.title)
driver.find_element_by_xpath("//div[@id = 'block-block-3']//descendant::a[text()='Read more']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[text()='Contact us']").click()
driver.find_element_by_id('edit-name').send_keys("123asdasd")
sleep(5)
driver.quit()