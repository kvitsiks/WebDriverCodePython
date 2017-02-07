from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.portnov.com')
driver.find_element_by_link_text("")